## 2026-04-28 — compare-countries notebook

- Added `notebooks/compare_countries.ipynb` implementing Task 3 KPIs and cross-country comparison.
  - Loads cleaned CSVs for Ethiopia, Kenya, Nigeria, Sudan, and Tanzania and concatenates them.
  - Computes monthly and annual summaries for temperature (`T2M`) and precipitation (`PRECTOTCORR`).
  - Produces visualizations: monthly temperature trends, precipitation variability boxplots, extreme-heat counts, and consecutive dry-day statistics.
  - Performs statistical tests (ANOVA / Kruskal) on monthly metrics and compiles a vulnerability ranking with COP32-ready observations.

- Files changed: `notebooks/compare_countries.ipynb` (outputs executed and saved).

- Notes:
  - The notebook expects cleaned CSVs in the `data/` directory (e.g., `ethiopia_clean.csv`). If those files are missing, some outputs will be empty; run the notebook locally to reproduce full outputs.
  - CI contains lightweight smoke tests and was not modified by this merge.

Author: kidinuhame1-spec
