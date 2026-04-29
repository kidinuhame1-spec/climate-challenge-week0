import sys
import pathlib
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Ensure repo root is on sys.path so `import app` works when Streamlit runs the script
repo_root = pathlib.Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from app.utils import (
    load_country_data,
    filter_by_country_and_year,
    fetch_csv_from_url,
    normalize_dataframe,
)


st.set_page_config(layout="wide", page_title="Climate Vulnerability Dashboard")


@st.cache_data
def load_data():
    return load_country_data("data")


def main():
    st.title("Cross-Country Climate Comparison")
    df = load_data()
    # If no local data and no remote URLs provided, allow a code-only demo dataset
    def make_demo_data(start="2015-01-01", end="2020-12-31", countries=None):
        rng = pd.date_range(start=start, end=end, freq="D")
        if countries is None:
            countries = ["Ethiopia", "Kenya", "Nigeria", "Sudan", "Tanzania"]
        rows = []
        for c in countries:
            # base temp varies by country
            base = {
                "Ethiopia": 16,
                "Kenya": 20,
                "Nigeria": 26,
                "Sudan": 28,
                "Tanzania": 27,
            }.get(c, 22)
            for d in rng:
                t2m = base + 5 * np.sin(2 * np.pi * (d.timetuple().tm_yday) / 365) + np.random.normal(0, 1)
                pre = max(0, np.random.gamma(1.2, 1.5))
                rows.append({"time": d, "country": c, "T2M": round(t2m, 2), "PRECTOTCORR": round(pre, 2)})
        return pd.DataFrame(rows)
    # Allow loading remote CSV(s) via URL(s) (e.g., Google Drive share links)
    urls_text = st.sidebar.text_area(
        "Remote CSV URLs (one per line, optional)", value="", height=80
    )
    if urls_text.strip():
        urls = [u.strip() for u in urls_text.splitlines() if u.strip()]
        dfs = []
        errors = []
        for u in urls:
            try:
                st.sidebar.info(f"Loading: {u}")
                remote_df = fetch_csv_from_url(u)
                # normalize columns (country/time inference) and record source
                remote_df = normalize_dataframe(remote_df, source_name=u)
                remote_df["source_file"] = u
                dfs.append(remote_df)
            except Exception as e:
                errors.append((u, str(e)))

        if not dfs and errors:
            for u, msg in errors:
                st.sidebar.error(f"{u}: {msg}")
            return

        if dfs:
            # concatenate remote CSVs and prefer remote data over local
            df_remote = pd.concat(dfs, ignore_index=True)
            df = df_remote
            if errors:
                for u, msg in errors:
                    st.sidebar.warning(f"Partial failure: {u}: {msg}")
    if df.empty:
        st.warning("No local data found in `data/`. You can paste remote CSV URLs in the sidebar.")
        if st.sidebar.button("Use code-only demo data"):
            df = make_demo_data()
            st.sidebar.success("Demo data generated — running in demo mode.")
        else:
            return

    # Defensive: if CSVs lack an explicit `country` column, try to infer it
    # from the `source_file` column (e.g. 'ethiopia_clean.csv' -> 'Ethiopia').
    if "country" not in df.columns:
        if "source_file" in df.columns:
            df = df.copy()
            df["country"] = df["source_file"].apply(
                lambda s: pathlib.Path(s).stem.replace("_clean", "").replace("_", " ").replace("-", " ").title()
            )
            st.info("Inferred `country` from `source_file` column.")
        else:
            st.warning(
                "No `country` column found and no `source_file` to infer from.\n"
                "Ensure your CSVs contain a `country` column or are named like '<country>_clean.csv'."
            )
            return

    # Ensure there's a parseable time column for filtering and plotting
    if "time" not in df.columns:
        st.warning(
            "No `time` column found in the data. The app requires a `time` column with parseable timestamps."
        )
        return

    # Convert `time` to datetime if necessary and ensure parsing succeeded
    df = df.copy()
    df["time"] = pd.to_datetime(df["time"], errors="coerce")
    if df["time"].isna().all():
        st.warning(
            "Could not parse any values in the `time` column. Ensure timestamps are in a standard format (ISO, YYYY-MM-DD, etc.)."
        )
        return

    # Display a concise data summary for debugging and user awareness
    n_rows = len(df)
    n_parseable = int(df["time"].notna().sum())
    n_countries = int(df["country"].nunique())
    st.sidebar.markdown("**Data summary**")
    st.sidebar.write(f"Rows: {n_rows}")
    st.sidebar.write(f"Parseable times: {n_parseable}")
    st.sidebar.write(f"Countries: {n_countries}")

    countries = sorted(df["country"].dropna().unique().tolist())

    with st.sidebar:
        st.header("Controls")
        sel_countries = st.multiselect("Select countries", countries, default=countries)
        min_year = int(df["time"].dt.year.min())
        max_year = int(df["time"].dt.year.max())
        year_range = st.slider("Year range", min_year, max_year, (min_year, max_year))
        var = st.selectbox("Variable", ["T2M", "PRECTOTCORR", "RH2M"], index=0)

    filtered = filter_by_country_and_year(df, sel_countries, year_range)

    st.subheader(f"{var} trend")
    if var in filtered.columns:
        trend = (
            filtered.dropna(subset=[var])
            .groupby([pd.Grouper(key="time", freq="ME"), "country"])[var]
            .mean()
            .reset_index()
        )
        chart = alt.Chart(trend).mark_line().encode(
            x=alt.X("time:T", title="Time"),
            y=alt.Y(f"{var}:Q", title=f"{var}"),
            color="country:N",
            tooltip=["time:T", "country:N", alt.Tooltip(f"{var}:Q", title=var)],
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info(f"{var} not available in dataset.")

    st.subheader(f"{var} distribution")
    if var in filtered.columns:
        box = alt.Chart(filtered.dropna(subset=[var])).mark_boxplot().encode(
            x=alt.X("country:N", title="Country"),
            y=alt.Y(f"{var}:Q", title=var),
            color="country:N",
            tooltip=["country:N", alt.Tooltip(f"{var}:Q", title=var)],
        )
        st.altair_chart(box, use_container_width=True)
    else:
        st.info(f"{var} not available in dataset.")

    st.markdown("---")
    st.subheader("Data preview")
    st.dataframe(filtered.head(200))


if __name__ == "__main__":
    main()
