# Climate Challenge Week 0

Repository for the 10 Academy KAIM Week 0 climate challenge, covering project setup, data profiling, cleaning, and country-level exploratory data analysis on African climate datasets.

## Project overview

This repository contains my implementation for the Week 0 challenge using climate data for:

- Ethiopia
- Kenya
- Sudan
- Tanzania
- Nigeria

The work completed in this repository includes:

- Task 1: Git and environment setup
- Task 2: Data profiling, cleaning, and country-specific EDA notebooks

## Implemented work

### Task 1: Git & environment setup

- Created the required repository structure for notebooks, scripts, source files, tests, and VS Code settings
- Added `.gitignore`, `requirements.txt`, `README.md`, and GitHub Actions CI workflow
- Configured CI to run on push to `main`
- Documented environment reproduction steps in this README

### Task 2: Data profiling, cleaning, and EDA

- Created one notebook per country:
  - `notebooks/ethiopia_eda.ipynb`
  - `notebooks/kenya_eda.ipynb`
  - `notebooks/sudan_eda.ipynb`
  - `notebooks/tanzania_eda.ipynb`
  - `notebooks/nigeria_eda.ipynb`
- Implemented data loading, date parsing, missing-value handling, duplicate checks, outlier detection, cleaned CSV export, and required visualizations for each country
- Kept `data/` and CSV outputs out of version control in accordance with the challenge instruction

## Environment setup

### Prerequisites
- Python 3.10+
- Git

### Reproduce the environment (Windows PowerShell)
1. `git clone <your-repo-url>`
2. `cd climate-challenge-week0`
3. `python -m venv venv`
4. `.\venv\Scripts\Activate.ps1`
5. `pip install -r requirements.txt`

### Reproduce the environment (macOS/Linux)
1. `git clone <your-repo-url>`
2. `cd climate-challenge-week0`
# Climate Challenge Week 0

Repository for the 10 Academy KAIM Week 0 climate challenge, covering project setup, data profiling, cleaning, and country-level exploratory data analysis on African climate datasets.

## Project overview

This repository contains my implementation for the Week 0 challenge using climate data for:

- Ethiopia
- Kenya
- Sudan
- Tanzania
- Nigeria

The work completed in this repository includes:

- Task 1: Git and environment setup
- Task 2: Data profiling, cleaning, and country-specific EDA notebooks

## Implemented work

### Task 1: Git & environment setup

- Created the required repository structure for notebooks, scripts, source files, tests, and VS Code settings
- Added `.gitignore`, `requirements.txt`, `README.md`, and GitHub Actions CI workflow
- Configured CI to run on push to `main`
- Documented environment reproduction steps in this README

### Task 2: Data profiling, cleaning, and EDA

- Created one notebook per country:
  - `notebooks/ethiopia_eda.ipynb`
  - `notebooks/kenya_eda.ipynb`
  - `notebooks/sudan_eda.ipynb`
  - `notebooks/tanzania_eda.ipynb`
  - `notebooks/nigeria_eda.ipynb`
- Implemented data loading, date parsing, missing-value handling, duplicate checks, outlier detection, cleaned CSV export, and required visualizations for each country
- Kept `data/` and CSV outputs out of version control in accordance with the challenge instruction

## Environment setup

### Prerequisites
- Python 3.10+
- Git

### Reproduce the environment (Windows PowerShell)
1. `git clone <your-repo-url>`
2. `cd climate-challenge-week0`
3. `python -m venv venv`
4. `.
venv\Scripts\Activate.ps1`
5. `pip install -r requirements.txt`

### Reproduce the environment (macOS/Linux)
1. `git clone <your-repo-url>`
2. `cd climate-challenge-week0`
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`

## Project structure

```text
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
+  └── README.md
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```

## Contribution evidence

- Branch used: `setup-task`
- Required files included: `.gitignore`, `requirements.txt`, `.github/workflows/ci.yml`
- Merge method: Pull Request into `main`
- Task 2 notebooks merged into `main` after implementation on a dedicated working branch

## Development Setup (quick)

Follow these steps to create a reproducible development environment and run tests locally.

- Create a virtual environment:

  - Windows PowerShell:

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

  - macOS / Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

- Run tests locally:

  ```bash
  pytest -q
  ```

Notes:
- CI is configured in `.github/workflows/ci.yml` to run `pytest` on push and pull requests to `main`.
- Do not push changes until you are ready to open a Pull Request from the `setup-task` branch.

## Streamlit Dashboard (dashboard-dev)

This repository includes a minimal Streamlit dashboard implemented at `app/main.py` intended for cross-country climate comparisons.

- Branch: `dashboard-dev` (development branch for the dashboard features).
- Commit: `feat: basic Streamlit UI` — adds `app/main.py` and `app/utils.py` with the dashboard UI.

Features
- Country multi-select widget (sidebar).
- Year range slider (sidebar).
- Temperature trend line chart (monthly averages, Altair).
- Precipitation distribution boxplot (Altair boxplot).

Notes about data
- The `data/` folder is intentionally git-ignored (contains cleaned CSVs). The app reads local CSVs from `data/` when run locally.
- For deployment on Streamlit Community Cloud either commit a small sample CSV under `data/` (for demo) or modify the app to fetch remote data (recommended for real deployments).

Run locally
```bash
pip install -r requirements.txt
streamlit run app/main.py
```

Deploy to Streamlit Community Cloud
1. Push your branch (e.g., `dashboard-dev`) to GitHub.
2. Go to https://share.streamlit.io/new and select the repository and branch.
3. Set **Main file path** to `app/main.py` and click **Deploy**.

Development notes
- Keep `data/` ignored to avoid committing large datasets. Use environment secrets or remote storage for production data access.
