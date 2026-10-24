# Person1 - LA2 NEON nitrate forecasting package

**Assigned sites:** BIGC, BLDE, BLUE

## Deliverables

- `reports/Person1_LA2_Report.pdf` - report with problem statement, dataset, methodology, results, conclusion, tables, plots and references.
- `notebooks/Person1_LA2_PySpark.ipynb` - full runnable PySpark/Spark MLlib notebook.
- `source/Person1_LA2_PySpark.py` and `source/Person1_LA2_PySpark_Source.pdf` - printable/exported source code.
- `dataset/raw/<SITE>/` - selected original NEON measurement CSV files matching `*NSW_15_minute*.csv`.
- `dataset/metadata/` - NEON variables/readme supporting documents.
- `dataset/source_manifest.csv` - original archive paths and local extracted paths.
- `dataset/data_dictionary.csv` - feature and target definitions.
- `dataset/derived_preview/` - optional prepared 30-minute tables for inspection; the notebook rebuilds the inputs from the raw files.
- `outputs/tables/` and `outputs/figures/` - data audit plus real local reference benchmark results and plots.

## Research question

Can accepted historical nitrate values at 30-minute resolution predict `surfWaterNitrateMean` 24 hours and 7 days ahead at these three NEON sites? Target units are micromoles per liter (µmol/L).

## Run the notebook

1. Extract this ZIP and open the `.ipynb` in Jupyter. Start Jupyter from this folder or let the notebook locate the parent project folder.
2. Install dependencies from `requirements.txt` and ensure a compatible Java/Spark installation is available.
3. Run all cells top-to-bottom. The notebook reads from `dataset/raw/` and writes Spark-native model metrics, per-site metrics, a runtime/scalability table, and plots to `outputs/`.
4. For the final submission, use the Spark-generated `model_metrics_spark.csv`, `site_model_metrics_spark.csv`, and `scalability_results_spark.csv` outputs from your actual run.

## Models and evaluation

Three Spark MLlib regressors: Linear Regression, Random Forest Regressor, Gradient-Boosted Trees Regressor. Baselines: persistence and seasonal naive. Metrics: MAE, RMSE and R². Forecast horizons: 24h and 7d. A per-site chronological 80/20 split is used; training labels cannot cross the site's cutoff.

## Important benchmark note

Files ending in `_reference.csv` / `_reference.png` are real local **scikit-learn reference** results calculated in the build environment from the same 30-minute feature definition using a 5,000-row training subsample. Their runtimes are not Spark timings. The notebook produces the authoritative Spark MLlib metrics and machine-specific execution-time/scalability measurements when run. Do not describe the reference timings as Spark results.

## Data-quality notes

NEON product page: https://data.neonscience.org/data-products/DP1.20033.001. The product contains 15-minute nitrate averages, and NEON defines `finalQF=0` as pass and `finalQF=1` as fail. The pipeline retains valid nonnegative nitrate values where `finalQF==0`, removes duplicate site/timestamp rows, aggregates accepted measurements into 30-minute bins, and retains partial bins with `valid_15min_count` showing whether one or two accepted 15-minute observations are available. For publication, run a sensitivity analysis restricted to two-observation bins and verify the release/issue log because NEON announced a nitrate-processing and quality-flag update in June 2026.
