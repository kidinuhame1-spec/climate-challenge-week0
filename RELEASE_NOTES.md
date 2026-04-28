# Release v0.1.0 — 2026-04-28

This release packages the initial analysis work for Task 3: cross-country KPI comparisons and a vulnerability ranking intended for COP32 briefing.

Highlights
- Added `notebooks/compare_countries.ipynb` which:
  - Loads cleaned CSVs for Ethiopia, Kenya, Nigeria, Sudan, and Tanzania and concatenates them.
  - Computes monthly and annual summaries for temperature (`T2M`) and precipitation (`PRECTOTCORR`).
  - Produces visualizations: monthly temperature trends, precipitation variability boxplots, extreme-heat counts, and consecutive dry-day statistics.
  - Runs statistical tests (ANOVA / Kruskal) and compiles a vulnerability ranking with COP32-ready observations.

Notes
- The notebook requires cleaned CSVs in `data/` (e.g., `ethiopia_clean.csv`) to reproduce full outputs.
- CI contains lightweight smoke tests and was not modified by this release.

Files
- notebooks/compare_countries.ipynb (executed outputs included)
- CHANGELOG.md (merge notes)

How to reproduce
1. Create a Python environment and install requirements (see `requirements.txt`).
2. Ensure cleaned CSVs are present under `data/`.
3. Run the notebook locally or with `jupyter nbconvert --to notebook --inplace --execute notebooks/compare_countries.ipynb`.

Acknowledgments
- Analysis and notebook authored by kidinuhame1-spec.
