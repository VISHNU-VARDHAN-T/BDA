# Dataset source and preprocessing - Person1

- Source: NEON Nitrate in Surface Water, data product DP1.20033.001: https://data.neonscience.org/data-products/DP1.20033.001
- Official quick start: https://data.neonscience.org/api/v0/documents/quick-start-guides/NEON.QSG.DP1.20033.001v1?fallback=html&inline=true
- Assigned sites: BIGC, BLDE, BLUE.
- Original input tables: `raw/<SITE>/*NSW_15_minute*.csv`. The included raw CSVs are source measurements; `metadata/variables.csv` and `metadata/readme.txt` are supporting product documentation.
- Target basis: `surfWaterNitrateMean`, reported in micromoles per liter (µmol/L).
- Filtering: parse UTC timestamps; keep numeric nonnegative means with `finalQF == 0` (NEON's flag definition says 0=pass and 1=fail); remove duplicate `(siteID, startDateTime)` rows.
- Aggregation: group valid source rows into non-overlapping 30-minute windows, store the window end time as `time`, and compute mean nitrate plus available minima, maxima, uncertainty, standard error and valid source-row count. Partial bins with one accepted 15-minute input are retained and flagged by `valid_15min_count`.
- Features: current completed-bin nitrate, lags at 30 minutes/1 hour/24 hours/7 days, measurement summary fields, hour/day-of-year sine/cosine features and month.
- Labels: exact observed mean at `time + 24 hours` or `time + 7 days`; missing future windows remain unlabeled rather than interpolated.
- Split: per-site chronological 80/20 split; training target times must remain strictly before the site's cutoff.
- The `derived_preview` subfolder is only for inspection. The notebook rebuilds its modelling data from original raw measurement files.

NEON notes that its nitrate product reports burst measurements as 15-minute averages and recommends using measurements whose final quality flag is 0. Check the current data-product issue log before publication, especially the 2026 quality-flag algorithm update.
