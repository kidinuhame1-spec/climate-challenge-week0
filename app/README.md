# Streamlit Dashboard — Deployment

This document describes how to deploy the Streamlit dashboard (`app/main.py`) to Streamlit Community Cloud.

Prerequisites
- A GitHub account with the repository pushed to GitHub.
- `requirements.txt` in the repo includes `streamlit` and `altair` (or add them before deploying).

Quick steps
1. Ensure the repo is pushed to GitHub and the dashboard branch is available (e.g., `dashboard-dev`).
2. Confirm `app/main.py` is the app entrypoint. The app reads local CSVs from the `data/` folder which is git-ignored.
3. If your app requires additional packages, add them to `requirements.txt`.
4. Visit https://streamlit.io/cloud and sign in with GitHub.
5. Click **New app**, choose the repository, select the branch (e.g., `dashboard-dev`), and set the **Main file path** to `app/main.py`.
6. Click **Deploy**. Streamlit will build the environment and serve the app.

Notes and tips
- The `data/` folder is ignored by git to avoid committing large datasets. For deployment, either:
  - commit a small sample dataset in `data/` for demo purposes (not recommended for large files), or
  - modify the app to fetch remote data (S3/HTTP) using environment secrets.
- To set secrets (API keys or URLs) for the app, go to the app settings on Streamlit Cloud and add them under **Secrets**.
- If your app requires a specific Python version or system packages, configure those in the Streamlit Cloud settings.

Local run
```bash
pip install -r requirements.txt
streamlit run app/main.py
```
