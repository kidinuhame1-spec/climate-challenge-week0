Branch: dashboard-dev

Commit: feat: basic Streamlit UI

Files added/updated:
- app/main.py — Streamlit app entrypoint with sidebar controls and Altair charts
- app/utils.py — data loading and filtering helpers
- requirements.txt — ensures `streamlit` and `altair` are listed for deployment

How to reproduce locally:
1. Create and activate Python virtual environment
2. pip install -r requirements.txt
3. streamlit run app/main.py

Purpose:
Provide a lightweight, reproducible Streamlit UI for cross-country climate comparisons. The app expects cleaned CSVs to exist in `data/` (these are git-ignored). For public deployment, use a small sample dataset or remote data sources.
