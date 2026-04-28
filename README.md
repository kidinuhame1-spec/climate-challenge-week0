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
│   └── README.md
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```

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
3. `python3 -m venv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`

## Contribution evidence

- Branch used: `setup-task`
- Required files included: `.gitignore`, `requirements.txt`, `.github/workflows/ci.yml`
- Merge method: Pull Request into `main`
- Task 2 notebooks merged into `main` after implementation on a dedicated working branch