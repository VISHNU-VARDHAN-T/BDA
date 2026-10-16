# BDA NEON Ecosystem Anomaly Detection — Region Scripts and Visualizations

## Files
- `Region_1_Algorithms.py`: Isolation Forest, LOF, HBOS
- `Region_2_Algorithms.py`: COPOD, KNN, DBSCAN
- `Region_3_Algorithms.py`: One-Class SVM, robust covariance/Mahalanobis fallback, PCA reconstruction error
- `bda_visualizations.py`: shared plotting helper required by all three scripts

Keep these four Python files in the same folder. Each script reads the corresponding regional `model_input_analytes_wide.csv` created by `classify_neon_regions.py`.

## Install dependencies
```bash
python -m pip install pandas numpy scikit-learn matplotlib seaborn pyod
```

## Run
From the folder containing these files and `BDA_NEON_Regional_Data/`:
```bash
python Region_1_Algorithms.py
python Region_2_Algorithms.py
python Region_3_Algorithms.py
```

For Jupyter, run `!python Region_1_Algorithms.py`, etc., in a Python kernel. If using an Apache Toree PySpark kernel, these scripts still need a Python interpreter with the listed dependencies; run the scripts from a terminal or Python kernel if PyOD is not available in Toree.

## Generated outputs
Each regional `model_results/` folder contains model scores and flags, the list of model features, plot PNGs in `plots/`, a site anomaly summary if siteID is present, and the top-100 suspicious samples if model score columns are available.

Plots attempted when the needed data exists:
1. Missingness by feature
2. Histograms with KDE
3. Boxplots
4. Violin plots
5. Correlation heatmap
6. Pairplot
7. 2D PCA
8. 3D PCA
9. Per-algorithm prediction counts
10. Anomaly score distributions
11. Anomaly score boxplots
12. Feature values by consensus anomaly flag
13. Anomaly rate by site
14. Anomaly count by site
15. Monthly anomaly counts
16. Monthly anomaly rate
17. Seasonal anomaly rate
18. Anomaly score over time
19. Parallel coordinates
20. Anomaly-flag heatmap

Some plots are omitted automatically if input columns or sample counts don't support them. Plots are exploratory; flagged records are potential anomalies, not confirmed ecological events. Check field names, units, dates, duplicate sample handling, and NEON data-product documentation before interpreting.

## Notes
- Input paths in the scripts match the output paths configured in `classify_neon_regions.py`.
- Features are numeric columns excluding common identifiers, date/time fields, site labels, and coordinate fields.
- Median imputation and standardization are performed within each region.
- The consensus flag means at least 2 of 3 region-specific detectors flagged the row. It is a heuristic for review, not ground truth.
- Region 2 DBSCAN uses an initial `eps=1.5` after standardization; tune it rather than treating it as universally optimal.
- For a fair cross-region anomaly-rate comparison, run at least one shared baseline algorithm and consistent preprocessing across all regions.
