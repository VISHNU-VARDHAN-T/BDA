from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from pyod.models.copod import COPOD
from pyod.models.knn import KNN
from bda_visualizations import create_visualizations

INPUT = Path('BDA_NEON_Regional_Data/Region_2_Southeast/model_input_analytes_wide.csv')
OUTPUT = Path('BDA_NEON_Regional_Data/Region_2_Southeast/model_results')
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
    models = {
        'COPOD': COPOD(),
        'KNN': KNN(contamination=0.05, n_neighbors=min(5, len(df)-1))
    }
    results = df.copy()
    for name, model in models.items():
        model.fit(Xs)
        results[f'{name}_anomaly'] = model.labels_.astype(int)
        results[f'{name}_score'] = np.asarray(model.decision_scores_).ravel()
    min_samples = max(5, min(10, len(df)-1))
    dbscan = DBSCAN(eps=1.5, min_samples=min_samples)
    clusters = dbscan.fit_predict(Xs)
    results['DBSCAN_cluster'] = clusters
    results['DBSCAN_anomaly'] = (clusters == -1).astype(int)
    core = Xs[dbscan.core_sample_indices_]
    if len(core):
        nearest = NearestNeighbors(n_neighbors=1).fit(core)
        results['DBSCAN_score'] = nearest.kneighbors(Xs)[0].ravel()
    else:
        results['DBSCAN_score'] = (clusters == -1).astype(float)
    model_names = ['COPOD', 'KNN', 'DBSCAN']
    labels = [f'{name}_anomaly' for name in model_names]
    results['anomaly_votes'] = results[labels].sum(axis=1)
    results['consensus_anomaly'] = (results['anomaly_votes'] >= 2).astype(int)
    results.to_csv(OUTPUT / 'region2_all_algorithm_results.csv', index=False)
    pd.DataFrame({'feature': features}).to_csv(OUTPUT / 'model_features_used.csv', index=False)
    create_visualizations(df, Xraw, Xs, results, features, model_names, OUTPUT / 'plots', 'Region 2 - Southeast')
    print('Region 2 completed')
    print('Samples:', len(df), '| Features:', len(features))
    print('DBSCAN clusters including -1 noise:', np.unique(clusters))
    print(results['anomaly_votes'].value_counts().sort_index())
    print('Results:', (OUTPUT / 'region2_all_algorithm_results.csv').resolve())
    print('DBSCAN uses initial eps=1.5 on scaled features; tune it with a k-distance plot.')

if __name__ == '__main__':
    main()
