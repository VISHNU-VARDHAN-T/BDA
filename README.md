# NEON regional data prepared for BDA

Source data product: NEON Chemical Properties of Surface Water (DP1.20093.001).

Only four model-relevant table types were copied: `swc_externalLabDataByAnalyte` (primary chemistry features), `swc_domainLabData` (domain-lab chemistry), `swc_fieldData` (field values and sample IDs), and `swc_fieldSuperParent` (sampling-event context). Validation files, categorical-code tables, variables dictionaries, readmes, EML XML, manifests, and absorbance scans were not copied.

Each region contains three site folders with the combined monthly rows for each selected table, plus `model_input_analytes_long.csv` and `model_input_analytes_wide.csv` where the analyte fields were identifiable. The wide matrix keeps analyte names and units separate; identifier/date columns are not model features.

The original download is not modified. Files with the same site/table/month were deduplicated by choosing the newest timestamp in the filename. See `reports/` for exact input file inventory, coverage, and site manifests.

These are candidate study clusters, not a guarantee that all sites within a cluster are immediate neighbours. Validate official coordinates and overlapping temporal coverage before making strict spatial claims.
