from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from pandas.plotting import parallel_coordinates

sns.set_theme(style='whitegrid', context='notebook')


def _normalise(name):
    return ''.join(ch.lower() for ch in str(name) if ch.isalnum())


def _find_column(df, candidates):
    lookup = {_normalise(c): c for c in df.columns}
    for candidate in candidates:
        key = _normalise(candidate)
        if key in lookup:
            return lookup[key]
    return None


def _save(fig, path):
    fig.tight_layout()
    fig.savefig(path, dpi=160, bbox_inches='tight')
    plt.close(fig)


def create_visualizations(raw_df, feature_frame, X_scaled, results, feature_cols,
                          model_names, output_dir, region_name):
    """Create robust overview, anomaly, feature, site and time-series plots."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    if not feature_cols or len(results) == 0:
        print('No feature data available for plots.')
        return

    plot_df = raw_df.loc[feature_frame.index].copy() if feature_frame.index.isin(raw_df.index).all() else raw_df.copy()
    # Align row order to the feature matrix / results.
    if len(plot_df) != len(results):
        plot_df = raw_df.iloc[:len(results)].copy()
    results_plot = results.reset_index(drop=True).copy()
    plot_df = plot_df.reset_index(drop=True)
    feature_frame = feature_frame.reset_index(drop=True)
    feature_cols = [c for c in feature_cols if c in feature_frame.columns]
    if not feature_cols:
        return

    anomaly_col = 'consensus_anomaly' if 'consensus_anomaly' in results_plot else None
    if anomaly_col is None:
        available_labels = [f'{m}_anomaly' for m in model_names if f'{m}_anomaly' in results_plot]
        if available_labels:
            results_plot['consensus_anomaly'] = (results_plot[available_labels].sum(axis=1) >= 1).astype(int)
            anomaly_col = 'consensus_anomaly'
    labels = results_plot[anomaly_col].astype(int).to_numpy() if anomaly_col else np.zeros(len(results_plot), dtype=int)

    # Choose a small, informative subset when there are many analytes.
    variance = feature_frame[feature_cols].var(numeric_only=True).sort_values(ascending=False)
    top_features = variance.index.tolist()[:min(12, len(variance))]
    top_features_8 = top_features[:8]
    top_features_5 = top_features[:5]

    # 1. Missingness.
    miss = raw_df[[c for c in feature_cols if c in raw_df.columns]].isna().mean().sort_values(ascending=False).head(30)
    if len(miss):
        fig, ax = plt.subplots(figsize=(max(9, 0.45 * len(miss)), 5))
        miss.mul(100).sort_values().plot(kind='barh', ax=ax)
        ax.set_title(f'{region_name}: Missing values by feature (top 30)')
        ax.set_xlabel('Missing values (%)')
        ax.set_ylabel('Feature')
        _save(fig, out / '01_missingness_by_feature.png')

    # 2. Histograms with KDE.
    if top_features:
        ncols = 3
        nrows = int(np.ceil(len(top_features) / ncols))
        fig, axes = plt.subplots(nrows, ncols, figsize=(15, 4 * nrows))
        axes = np.array(axes).reshape(-1)
        for ax, col in zip(axes, top_features):
            vals = feature_frame[col].dropna()
            sns.histplot(vals, kde=len(vals) > 2, color='steelblue', ax=ax)
            ax.set_title(str(col)[:45])
        for ax in axes[len(top_features):]:
            ax.set_visible(False)
        fig.suptitle(f'{region_name}: Feature distributions', y=1.01)
        _save(fig, out / '02_feature_histograms_kde.png')

    # 3. Boxplots.
    if top_features_8:
        long = feature_frame[top_features_8].melt(var_name='Feature', value_name='Value')
        fig, ax = plt.subplots(figsize=(max(11, len(top_features_8) * 1.4), 6))
        sns.boxplot(data=long, x='Feature', y='Value', color='steelblue', ax=ax, showfliers=True)
        ax.tick_params(axis='x', rotation=45)
        ax.set_title(f'{region_name}: Feature boxplots')
        _save(fig, out / '03_feature_boxplots.png')

    # 4. Violin plots.
    if top_features_8:
        long = feature_frame[top_features_8].melt(var_name='Feature', value_name='Value')
        fig, ax = plt.subplots(figsize=(max(11, len(top_features_8) * 1.4), 6))
        sns.violinplot(data=long, x='Feature', y='Value', color='steelblue', ax=ax, cut=0, inner='quartile')
        ax.tick_params(axis='x', rotation=45)
        ax.set_title(f'{region_name}: Feature violin plots')
        _save(fig, out / '04_feature_violinplots.png')

    # 5. Correlation heatmap.
    corr_features = variance.index.tolist()[:min(25, len(variance))]
    if len(corr_features) >= 2:
        corr = feature_frame[corr_features].corr()
        fig, ax = plt.subplots(figsize=(max(9, len(corr_features) * 0.55), max(7, len(corr_features) * 0.45)))
        sns.heatmap(corr, cmap='vlag', center=0, annot=len(corr_features) <= 12,
                    fmt='.2f', square=False, ax=ax)
        ax.set_title(f'{region_name}: Chemical-feature correlation heatmap')
        _save(fig, out / '05_correlation_heatmap.png')

    # 6. Pairplot.
    if len(top_features_5) >= 2:
        pair_df = feature_frame[top_features_5].copy()
        pair_df['Anomaly'] = np.where(labels == 1, 'Potential anomaly', 'Other')
        if len(pair_df) > 700:
            pair_df = pair_df.sample(700, random_state=42)
        try:
            grid = sns.pairplot(pair_df, vars=top_features_5, hue='Anomaly', corner=True,
                                diag_kind='hist', plot_kws={'s': 18, 'alpha': 0.65})
            grid.fig.suptitle(f'{region_name}: Pairwise feature relationships', y=1.02)
            grid.fig.savefig(out / '06_pairplot.png', dpi=140, bbox_inches='tight')
            plt.close(grid.fig)
        except Exception as exc:
            warnings.warn(f'Pairplot skipped: {exc}')

    # 7. PCA 2D and 3D.
    n_components = min(3, X_scaled.shape[1], X_scaled.shape[0])
    if n_components >= 2:
        pca = PCA(n_components=n_components, random_state=42)
        coords = pca.fit_transform(X_scaled)
        pca_df = pd.DataFrame({'PC1': coords[:, 0], 'PC2': coords[:, 1],
                               'Anomaly': np.where(labels == 1, 'Potential anomaly', 'Other')})
        fig, ax = plt.subplots(figsize=(9, 7))
        sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Anomaly', alpha=0.75, s=35, ax=ax)
        ax.set_title(f'{region_name}: PCA projection (variance explained {pca.explained_variance_ratio_[:2].sum():.1%})')
        _save(fig, out / '07_pca_2d.png')
        if n_components >= 3:
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            for label, color in [(0, 'tab:blue'), (1, 'tab:red')]:
                mask = labels == label
                ax.scatter(coords[mask, 0], coords[mask, 1], coords[mask, 2],
                           label='Potential anomaly' if label else 'Other', alpha=0.7, s=25)
            ax.set_xlabel('PC1'); ax.set_ylabel('PC2'); ax.set_zlabel('PC3')
            ax.set_title(f'{region_name}: 3D PCA projection')
            ax.legend()
            _save(fig, out / '08_pca_3d.png')

    # 8. Algorithm anomaly count and score distributions.
    label_cols = [f'{m}_anomaly' for m in model_names if f'{m}_anomaly' in results_plot]
    if label_cols:
        counts = pd.DataFrame({c.replace('_anomaly', ''): [int(results_plot[c].sum()), int((results_plot[c] == 0).sum())]
                               for c in label_cols}, index=['Potential anomaly', 'Other']).T
        fig, ax = plt.subplots(figsize=(10, 6))
        counts.plot(kind='bar', stacked=True, ax=ax)
        ax.set_title(f'{region_name}: Algorithm prediction counts')
        ax.set_ylabel('Samples')
        ax.tick_params(axis='x', rotation=25)
        _save(fig, out / '09_algorithm_prediction_counts.png')

    score_cols = [f'{m}_score' for m in model_names if f'{m}_score' in results_plot]
    if score_cols:
        ncols = 2
        nrows = int(np.ceil(len(score_cols) / ncols))
        fig, axes = plt.subplots(nrows, ncols, figsize=(13, 4 * nrows))
        axes = np.array(axes).reshape(-1)
        for ax, col in zip(axes, score_cols):
            sns.histplot(data=results_plot, x=col, hue=anomaly_col if anomaly_col else None,
                         element='step', stat='density', common_norm=False, palette={0: 'steelblue', 1: 'crimson'} if anomaly_col else None, ax=ax)
            ax.set_title(f'{col}: score distribution')
        for ax in axes[len(score_cols):]:
            ax.set_visible(False)
        fig.suptitle(f'{region_name}: Anomaly-score distributions', y=1.01)
        _save(fig, out / '10_anomaly_score_distributions.png')

        fig, ax = plt.subplots(figsize=(max(9, len(score_cols) * 1.5), 6))
        sns.boxplot(data=results_plot[score_cols], color='steelblue', ax=ax)
        ax.tick_params(axis='x', rotation=25)
        ax.set_title(f'{region_name}: Anomaly score comparison')
        _save(fig, out / '11_anomaly_score_boxplots.png')

    # 9. Feature distributions, potential anomalies vs others.
    if anomaly_col and top_features_8:
        plotdata = feature_frame[top_features_8].copy()
        plotdata['Detection'] = np.where(labels == 1, 'Potential anomaly', 'Other')
        long = plotdata.melt(id_vars='Detection', var_name='Feature', value_name='Value')
        fig, ax = plt.subplots(figsize=(max(12, len(top_features_8) * 1.5), 6))
        sns.boxplot(data=long, x='Feature', y='Value', hue='Detection', palette={'Other': 'steelblue', 'Potential anomaly': 'crimson'}, ax=ax)
        ax.tick_params(axis='x', rotation=45)
        ax.set_title(f'{region_name}: Feature values by consensus anomaly flag')
        _save(fig, out / '12_features_anomaly_vs_normal.png')

    # 10. Site-level anomaly counts/rates when site metadata exists.
    site_col = _find_column(results_plot, ['siteID', 'site_id', 'site', 'siteCode'])
    if site_col and anomaly_col:
        by_site = results_plot.groupby(site_col, dropna=False).agg(
            samples=(anomaly_col, 'size'),
            anomalies=(anomaly_col, 'sum')
        ).reset_index()
        by_site['anomaly_rate_pct'] = 100 * by_site['anomalies'] / by_site['samples'].clip(lower=1)
        by_site.to_csv(out / 'site_anomaly_summary.csv', index=False)
        fig, ax = plt.subplots(figsize=(9, 5))
        sns.barplot(data=by_site, x=site_col, y='anomaly_rate_pct', color='steelblue', ax=ax)
        ax.set_ylabel('Potential anomalies (%)')
        ax.set_title(f'{region_name}: Potential anomaly rate by site')
        _save(fig, out / '13_anomaly_rate_by_site.png')
        fig, ax = plt.subplots(figsize=(9, 5))
        sns.barplot(data=by_site, x=site_col, y='anomalies', color='steelblue', ax=ax)
        ax.set_ylabel('Potential anomaly samples')
        ax.set_title(f'{region_name}: Anomaly count by site')
        _save(fig, out / '14_anomaly_count_by_site.png')

    # 11. Time-series and seasonality plots when date column exists.
    date_col = _find_column(results_plot, [
        'collectDate', 'collectDateTime', 'sampleDate', 'sampleDateTime', 'date',
        'datetime', 'startDate', 'collectDateBegin', 'sampleStartDate', 'sampledDate'
    ])
    if date_col:
        dates = pd.to_datetime(results_plot[date_col], errors='coerce', utc=True).dt.tz_convert(None)
        temporal = results_plot.copy()
        temporal['_plot_date'] = dates
        temporal = temporal.dropna(subset=['_plot_date'])
        if len(temporal):
            temporal['_month'] = temporal['_plot_date'].dt.to_period('M').dt.to_timestamp()
            if anomaly_col:
                monthly = temporal.groupby('_month').agg(
                    samples=(anomaly_col, 'size'),
                    anomaly_count=(anomaly_col, 'sum'),
                    anomaly_rate=(anomaly_col, 'mean')
                ).reset_index()
                fig, ax = plt.subplots(figsize=(13, 5))
                ax.plot(monthly['_month'], monthly['anomaly_count'], marker='o', label='Anomaly count')
                ax.set_title(f'{region_name}: Monthly potential anomaly counts')
                ax.set_xlabel('Month'); ax.set_ylabel('Potential anomalies')
                ax.legend()
                _save(fig, out / '15_monthly_anomaly_counts.png')
                fig, ax = plt.subplots(figsize=(13, 5))
                ax.plot(monthly['_month'], 100 * monthly['anomaly_rate'], marker='o')
                ax.set_title(f'{region_name}: Monthly potential anomaly rate')
                ax.set_xlabel('Month'); ax.set_ylabel('Potential anomalies (%)')
                _save(fig, out / '16_monthly_anomaly_rate.png')
            temporal['_calendar_month'] = temporal['_plot_date'].dt.month
            if anomaly_col:
                season = temporal.groupby('_calendar_month')[anomaly_col].mean().mul(100).reindex(range(1, 13))
                fig, ax = plt.subplots(figsize=(10, 5))
                season.plot(kind='bar', ax=ax)
                ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], rotation=0)
                ax.set_title(f'{region_name}: Seasonal anomaly rate by calendar month')
                ax.set_ylabel('Potential anomalies (%)')
                _save(fig, out / '17_seasonality_anomaly_rate.png')
            score = score_cols[0] if score_cols else None
            if score:
                temporal[score] = pd.to_numeric(temporal[score], errors='coerce')
                score_month = temporal.groupby('_month')[score].mean()
                fig, ax = plt.subplots(figsize=(13, 5))
                score_month.plot(ax=ax, marker='o')
                ax.set_title(f'{region_name}: Mean {score} over time')
                ax.set_xlabel('Month'); ax.set_ylabel('Mean anomaly score')
                _save(fig, out / '18_anomaly_score_over_time.png')

    # 12. Parallel coordinates using up to five features.
    if len(top_features_5) >= 2:
        parallel = feature_frame[top_features_5].copy()
        for col in top_features_5:
            sd = parallel[col].std()
            parallel[col] = (parallel[col] - parallel[col].mean()) / (sd if sd and np.isfinite(sd) else 1)
        parallel['Detection'] = np.where(labels == 1, 'Potential anomaly', 'Other')
        if len(parallel) > 600:
            parallel = parallel.sample(600, random_state=42)
        fig, ax = plt.subplots(figsize=(13, 6))
        try:
            parallel_coordinates(parallel, 'Detection', ax=ax, alpha=0.35)
            ax.set_title(f'{region_name}: Parallel coordinates (standardized top features)')
            ax.set_ylabel('Standardized feature value')
            _save(fig, out / '19_parallel_coordinates.png')
        except Exception as exc:
            plt.close(fig)
            warnings.warn(f'Parallel coordinates skipped: {exc}')

    # 13. Algorithm-vote map per sample row.
    if label_cols:
        matrix = results_plot[label_cols].astype(int)
        if len(matrix) > 1500:
            matrix = matrix.iloc[:1500]
        fig, ax = plt.subplots(figsize=(max(8, len(label_cols) * 1.3), 7))
        sns.heatmap(matrix.T, cmap='vlag', center=0.5, cbar=False, ax=ax)
        ax.set_xlabel('Sample row (subset if >1500)')
        ax.set_ylabel('Algorithm')
        ax.set_title(f'{region_name}: Per-algorithm anomaly flags')
        _save(fig, out / '20_algorithm_flag_heatmap.png')

    # 14. Save the most suspicious samples and a compact plot index.
    score_cols_present = [c for c in score_cols if c in results_plot]
    if score_cols_present:
        score_rank = results_plot[score_cols_present].rank(pct=True).mean(axis=1)
        results_plot['mean_score_percentile'] = score_rank
        selected = results_plot.sort_values('mean_score_percentile', ascending=False).head(100)
        selected.to_csv(out / 'top_100_suspicious_samples.csv', index=False)

    index_lines = [f'Region: {region_name}', f'Samples plotted: {len(results_plot)}',
                   f'Feature count: {len(feature_cols)}', 'Plots are PNG files in this directory.']
    (out / 'PLOT_INDEX.txt').write_text('\n'.join(index_lines) + '\n', encoding='utf-8')
    print(f'Plots saved to: {out.resolve()}')
