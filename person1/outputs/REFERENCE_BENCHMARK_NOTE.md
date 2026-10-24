# Reference benchmark note

The files ending in `_reference.csv` and figures ending in `_reference.png` are real pilot measurements computed in the build environment with scikit-learn on the same 30-minute feature/target definitions. The pilot caps the fit subset at 5,000 training rows to keep the reference experiment portable and evaluates the chronological test rows. The wall-clock values are local scikit-learn reference timings, **not Spark execution-time measurements**.

The bundled notebook implements the required models in PySpark MLlib, runs on all available training rows, writes `model_metrics_spark.csv`, `site_model_metrics_spark.csv`, `scalability_results_spark.csv`, and produces Spark-native timing charts when executed. For a submission that reports Spark timings, run the notebook on the intended machine and use those generated Spark tables as the authoritative execution results.
