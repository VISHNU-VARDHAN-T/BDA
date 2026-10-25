# Reference benchmark note - Person2

These local reference results were measured using the three algorithms assigned to Person2. The reference implementation trained on up to 1,500 historical rows per site and evaluated on up to 2,000 holdout rows per site for each horizon. Training is chronologically before the test period, with future labels restricted to remain before the training cutoff.

The static table uses local Python estimator timings, not Spark MLlib training timings. PySpark performs source-data ingestion, quality control, aggregation, feature engineering and chronological splitting in the notebook. The individual estimators then run on the bounded stratified sample. After running the notebook, consult its `model_metrics_personal_models.csv`, `site_model_metrics_personal_models.csv` and `scalability_results_personal_models.csv` files; those timings belong to the machine used for the run.
