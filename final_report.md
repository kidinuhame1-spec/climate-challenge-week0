# Climate Challenge Week 0 — Final Report

By: Project Author

Published: April 2026

---

Summary

This report summarizes Week 0 of the climate challenge: repository setup, data cleaning and profiling, per-country exploratory analysis, and a small Streamlit dashboard for cross-country comparison. It is written in a concise, Medium-style narrative for reviewers and future readers.

Project highlights

- Assembled cleaned climate datasets for five countries (Ethiopia, Kenya, Nigeria, Sudan, Tanzania).
- Built reproducible notebooks per country covering data profiling, missing-value handling, and visual EDA.
- Implemented a lightweight Streamlit dashboard (`app/main.py`) with country multi-select, year-range slider, and variable selector for interactive cross-country views.
- Added robust CSV normalization and remote ingestion helpers to handle diverse file formats (including `YEAR+DOY` parsing).

Why it matters

Understanding climate variables across countries helps identify regional trends and potential data quality issues early. The dashboard provides an exploratory interface to compare temperature and precipitation patterns across countries and time ranges.

Data and methods

- Data sources: cleaned CSVs (kept out of version control) with consistent column naming where possible.
- Parsing: `app/utils.py` includes normalization logic to infer `country` and construct a `time` column from common patterns (`time/date/datetime`, `YEAR+Month+Day`, `YEAR+DOY`).
- Visualization: Altair for line charts (monthly averages) and boxplots (distributions). Pandas used for grouping and preprocessing.
- Demo mode: the app auto-generates a small demo dataset when no local CSVs are found so reviewers can run the dashboard without adding files.

Key files

- `app/main.py` — Streamlit entry point and UI controls.
- `app/utils.py` — CSV loaders, Google Drive fetcher, and normalization helpers.
- `notebooks/` — per-country notebooks and cross-country comparison notebook (`compare_countries.ipynb`).
- `README.md` — project overview and run instructions.

Dashboard walkthrough

1. Sidebar: paste one or more Google Drive share links (one per line) to load remote CSVs; use the country multi-select to choose which countries to view; adjust the year-range slider; pick a variable from the dropdown (e.g., `T2M`, `PRECTOTCORR`, `RH2M`).
2. Charts: the main view shows monthly trend lines (Altair) and a distribution boxplot for the selected variable.

Export & reproducibility

To produce a PDF copy of this report, you can:

- Use Pandoc (from the repo root):

```bash
pip install pandoc pypandoc
# convert markdown to PDF (requires a LaTeX toolchain like TinyTeX)
pandoc final_report.md -o final_report.pdf
```

- Or open `notebooks/final_report.ipynb` in Jupyter and use "File → Export Notebook As → PDF".

Submission artifacts

- GitHub: provide the URL to the `main` branch for evaluation. (If your dashboard work is on `dashboard-dev`, merge to `main` before submitting.)
- PDF: export this report as `final_report.pdf` and include it in the repository root or attach it to your submission.
- Screenshot: place a dashboard screenshot in `dashboard_screenshots/` (e.g., `dashboard_screenshots/dashboard.png`).

Next steps and reflections

- Add a CI smoke test to validate `app` imports and basic data normalization on push.
- Add a small, committed sample CSV (in `.git/info/exclude` or local-only) to make demos consistent for reviewers.
- Optionally, deploy the dashboard to Streamlit Community Cloud from the `dashboard-dev` branch.

---

If you want, I can convert this to a ready-to-download PDF and add a screenshot file to `dashboard_screenshots/` (you can upload the screenshot image or I can include a placeholder).