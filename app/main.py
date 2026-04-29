import sys
import pathlib
import streamlit as st
import pandas as pd
import altair as alt

# Ensure repo root is on sys.path so `import app` works when Streamlit runs the script
repo_root = pathlib.Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from app.utils import load_country_data, filter_by_country_and_year


st.set_page_config(layout="wide", page_title="Climate Vulnerability Dashboard")


@st.cache_data
def load_data():
    return load_country_data("data")


def main():
    st.title("Cross-Country Climate Comparison")
    df = load_data()
    if df.empty:
        st.warning("No data found in `data/`. Place cleaned CSVs there (they are git-ignored).")
        return

    countries = sorted(df["country"].dropna().unique().tolist())

    with st.sidebar:
        st.header("Controls")
        sel_countries = st.multiselect("Select countries", countries, default=countries)
        min_year = int(df["time"].dt.year.min())
        max_year = int(df["time"].dt.year.max())
        year_range = st.slider("Year range", min_year, max_year, (min_year, max_year))
        var = st.selectbox("Variable", ["T2M", "PRECTOTCORR", "RH2M"], index=0)

    filtered = filter_by_country_and_year(df, sel_countries, year_range)

    st.subheader("Temperature trend")
    if "T2M" in filtered.columns:
        temp = (
            filtered.dropna(subset=["T2M"]) 
            .groupby([pd.Grouper(key="time", freq="M"), "country"])["T2M"]
            .mean()
            .reset_index()
        )
        chart = alt.Chart(temp).mark_line().encode(
            x=alt.X("time:T", title="Time"),
            y=alt.Y("T2M:Q", title="T2M (°C)"),
            color="country:N",
            tooltip=["time:T", "country:N", "T2M:Q"],
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("T2M not available in dataset.")

    st.subheader("Precipitation distribution")
    if "PRECTOTCORR" in filtered.columns:
        box = alt.Chart(filtered.dropna(subset=["PRECTOTCORR"])).mark_boxplot().encode(
            x=alt.X("country:N", title="Country"),
            y=alt.Y("PRECTOTCORR:Q", title="PRECTOTCORR (mm)"),
            color="country:N",
            tooltip=["country:N", "PRECTOTCORR:Q"],
        )
        st.altair_chart(box, use_container_width=True)
    else:
        st.info("PRECTOTCORR not available in dataset.")

    st.markdown("---")
    st.subheader("Data preview")
    st.dataframe(filtered.head(200))


if __name__ == "__main__":
    main()
