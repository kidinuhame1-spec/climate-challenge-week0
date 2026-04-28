# Climate Challenge Week 0

Task 1 repository setup for the 10 Academy KAIM Week 0 challenge.

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

## Task 1 completion evidence

- Branch used: `setup-task`
- Required files included: `.gitignore`, `requirements.txt`, `.github/workflows/ci.yml`
- Merge method: Pull Request into `main`