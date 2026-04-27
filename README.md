# Climate Challenge Week 0

Repository setup for 10 Academy KAIM Week 0 climate challenge.

## Environment Reproducibility

### Prerequisites
- Python 3.10+
- Git

### Setup Steps (Windows PowerShell)
1. Clone the repository:
   `git clone <your-repo-url>`
2. Move into the project:
   `cd climate-challenge-week0`
3. Create a virtual environment:
   `python -m venv venv`
4. Activate it:
   `.\venv\Scripts\Activate.ps1`
5. Install dependencies:
   `pip install -r requirements.txt`

### Setup Steps (macOS/Linux)
1. Clone and enter the repository:
   `git clone <your-repo-url> && cd climate-challenge-week0`
2. Create and activate venv:
   `python3 -m venv venv`
   `source venv/bin/activate`
3. Install dependencies:
   `pip install -r requirements.txt`

## CI

GitHub Actions workflow lives at `.github/workflows/ci.yml` and runs dependency installation on pushes to `main`.

## Task 1 Checklist

- Create and use branch: `setup-task`
- Include `.gitignore`, `requirements.txt`, and CI workflow
- Keep `data/` and CSV files out of version control
- Merge `setup-task` into `main` via Pull Request