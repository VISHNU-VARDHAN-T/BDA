from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from sklearn.decomposition import PCA
from bda_visualizations import create_visualizations

INPUT = Path('BDA_NEON_Regional_Data/Region_3_Plains/model_input_analytes_wide.csv')
OUTPUT = Path('BDA_NEON_Regional_Data/Region_3_Plains/model_results')
OUTPUT.mkdir(parents=True, exist_ok=True)


def norm(s):
    return ''.join(ch.lower() for ch in str(s) if ch.isalnum())


def is_metadata(col):
    n = norm(col)
    exact = {'siteid','site','sitecode','region','sampleid','samplecode','eventid','uid','id',
             'collectdate','collectdatetime','sampledate','sampledatetime','date','datetime',
             'startdate','enddate','year','month','day','latitude','longitude','lat','lon',
             'easting','northing','utmzone','recordnumber','recordid','parentid','horizontaldatum'}
    return n in exact or any(x in n for x in ['latitude','longitude','datetime','timestamp','easting','northing'])


def main():
    df = pd.read_csv(INPUT)
    features = [c for c in df.select_dtypes(include=np.number).columns
                if not is_metadata(c) and df[c].nunique(dropna=True) > 1]
    if len(features) < 2:
        raise ValueError(f'Expected at least two numeric analyte features. Found: {features}')
    Xraw = df[features].replace([np.inf, -np.inf], np.nan).dropna(axis=1, how='all')
    features = Xraw.columns.tolist()
    keep = Xraw.notna().any(axis=1)
    df = df.loc[keep].reset_index(drop=True)
    Xraw = Xraw.loc[keep].reset_index(drop=True)
    X = SimpleImputer(strategy='median').fit_transform(Xraw)
    Xs = StandardScaler().fit_transform(X)
    if len(df) < 10:
        raise ValueError('At least 10 usable samples are recommended for this region.')
    results = df.copy()

    svm = OneClassSVM(kernel='rbf', nu=0.05, gamma='scale')
    svm.fit(Xs)
    svm_decision = svm.decision_function(Xs).ravel()
    results['OneClassSVM_score'] = -svm_decision
    results['OneClassSVM_anomaly'] = (svm_decision < 0).astype(int)

    n_cov = min(5, Xs.shape[1], max(1, (len(df)-1)//3))
    cov_pca = PCA(n_components=n_cov, random_state=42)
    X_cov = cov_pca.fit_transform(Xs)
    covariance = EllipticEnvelope(contamination=0.05, random_state=42)
    try:
        covariance.fit(X_cov)
        cov_pred = covariance.predict(X_cov)
        cov_score = -covariance.decision_function(X_cov)
    except Exception as exc:
        print(f'Warning: robust covariance failed ({exc}); falling back to PCA-space Mahalanobis distance.')
        center = X_cov.mean(axis=0)
        cov = np.cov(X_cov, rowvar=False)
        cov = np.atleast_2d(cov) + np.eye(X_cov.shape[1]) * 1e-6
        inv = np.linalg.pinv(cov)
        delta = X_cov - center
        cov_score = np.sqrt(np.maximum(0, np.einsum('ij,jk,ik->i', delta, inv, delta)))
        cov_threshold = np.quantile(cov_score, 0.95)
        cov_pred = np.where(cov_score >= cov_threshold, -1, 1)
    results['RobustCovariance_score'] = np.asarray(cov_score).ravel()
    results['RobustCovariance_anomaly'] = (np.asarray(cov_pred).ravel() == -1).astype(int)

    pca = PCA(n_components=0.95, svd_solver='full', random_state=42)
    X_reduced = pca.fit_transform(Xs)
    reconstructed = pca.inverse_transform(X_reduced)
    reconstruction_error = np.mean((Xs - reconstructed) ** 2, axis=1)
    threshold = np.quantile(reconstruction_error, 0.95)
    results['PCA_reconstruction_score'] = reconstruction_error
    results['PCA_reconstruction_anomaly'] = (reconstruction_error > threshold).astype(int)

    model_names = ['OneClassSVM', 'RobustCovariance', 'PCA_reconstruction']
    labels = [f'{name}_anomaly' for name in model_names]
    results['anomaly_votes'] = results[labels].sum(axis=1)
    results['consensus_anomaly'] = (results['anomaly_votes'] >= 2).astype(int)
    results.to_csv(OUTPUT / 'region3_all_algorithm_results.csv', index=False)
    pd.DataFrame({'feature': features}).to_csv(OUTPUT / 'model_features_used.csv', index=False)
    pd.DataFrame({'pca_component': range(1, len(pca.explained_variance_ratio_)+1),
                  'variance_explained': pca.explained_variance_ratio_}).to_csv(OUTPUT / 'pca_variance_explained.csv', index=False)
    create_visualizations(df, Xraw, Xs, results, features, model_names, OUTPUT / 'plots', 'Region 3 - Plains')
    print('Region 3 completed')
    print('Samples:', len(df), '| Features:', len(features))
    print('PCA components retained:', X_reduced.shape[1])
    print('PCA variance explained:', round(float(pca.explained_variance_ratio_.sum()), 4))
    print(results['anomaly_votes'].value_counts().sort_index())
    print('Results:', (OUTPUT / 'region3_all_algorithm_results.csv').resolve())

if __name__ == '__main__':
    main()
