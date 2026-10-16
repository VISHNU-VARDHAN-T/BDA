from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from pyod.models.iforest import IForest
from pyod.models.lof import LOF
from pyod.models.hbos import HBOS
from bda_visualizations import create_visualizations

INPUT = Path('BDA_NEON_Regional_Data/Region_1_Alabama/model_input_analytes_wide.csv')
OUTPUT = Path('BDA_NEON_Regional_Data/Region_1_Alabama/model_results')
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
    Xraw = df[features].replace([np.inf, -np.inf], np.nan)
    Xraw = Xraw.dropna(axis=1, how='all')
    features = Xraw.columns.tolist()
    keep = Xraw.notna().any(axis=1)
    df = df.loc[keep].reset_index(drop=True)
    Xraw = Xraw.loc[keep].reset_index(drop=True)
    X = SimpleImputer(strategy='median').fit_transform(Xraw)
    Xs = StandardScaler().fit_transform(X)
    if len(df) < 5:
        raise ValueError('At least 5 usable samples are recommended.')
    models = {
        'IsolationForest': IForest(contamination=0.05, random_state=42, n_estimators=250),
        'LOF': LOF(contamination=0.05, n_neighbors=min(20, max(2, len(df)-1))),
        'HBOS': HBOS(contamination=0.05, n_bins=10)
    }
    results = df.copy()
    for name, model in models.items():
        model.fit(Xs)
        results[f'{name}_anomaly'] = model.labels_.astype(int)
        results[f'{name}_score'] = np.asarray(model.decision_scores_).ravel()
    labels = [f'{name}_anomaly' for name in models]
    results['anomaly_votes'] = results[labels].sum(axis=1)
    results['consensus_anomaly'] = (results['anomaly_votes'] >= 2).astype(int)
    results.to_csv(OUTPUT / 'region1_all_algorithm_results.csv', index=False)
    pd.DataFrame({'feature': features}).to_csv(OUTPUT / 'model_features_used.csv', index=False)
    create_visualizations(df, Xraw, Xs, results, features, list(models), OUTPUT / 'plots', 'Region 1 - Alabama')
    print('Region 1 completed')
    print('Samples:', len(df), '| Features:', len(features))
    print('Anomaly votes:')
    print(results['anomaly_votes'].value_counts().sort_index())
    print('Results:', (OUTPUT / 'region1_all_algorithm_results.csv').resolve())

if __name__ == '__main__':
    main()
