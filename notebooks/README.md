# Notebooks

This folder stores per-country EDA notebooks and cross-country comparison notebooks.

## Task 3: Cross-country comparison

- `compare_countries.ipynb` — primary notebook for Task 3. It compares climate variables across countries, including trends and distributions for variables such as `T2M`, `PRECTOTCORR`, and `RH2M`.

Notebook list

- `ethiopia_eda.ipynb` — country-specific exploratory analysis for Ethiopia.
- `kenya_eda.ipynb` — country-specific exploratory analysis for Kenya.
- `nigeria_eda.ipynb` — country-specific exploratory analysis for Nigeria.
- `sudan_eda.ipynb` — country-specific exploratory analysis for Sudan.
- `tanzania_eda.ipynb` — country-specific exploratory analysis for Tanzania.
- `compare_countries.ipynb` — cross-country comparisons and summary (Task 3).

How to run

1. Create and activate a Python virtual environment and install dependencies:

```bash
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Start Jupyter Lab / Notebook from the repository root:

```bash
jupyter lab
# or
jupyter notebook
```

3. Open the notebook you want to run (e.g., `compare_countries.ipynb`) and run cells in order. The notebooks expect cleaned CSVs to be present in the top-level `data/` directory; if you don't have local CSVs the Streamlit app offers demo mode but the notebooks may require small sample files.

Inspect remote CSVs

Use `scripts/inspect_drive.py` to fetch and preview a Google Drive CSV (helpful when the notebook reports missing or unexpected columns):

```bash
python scripts/inspect_drive.py
```

Notes

- Notebooks were created with a Python 3 kernel; if you see parsing issues, verify `pandas` and `numpy` versions in `requirements.txt`.
- Keep `data/` git-ignored — do not commit large CSVs. For reproducible examples, add a small `data/sample.csv` locally (not committed) or modify notebooks to use the demo generator.

- compare_countries.ipynb: cross-country KPIs, statistical tests, vulnerability ranking, and COP32 observations.
