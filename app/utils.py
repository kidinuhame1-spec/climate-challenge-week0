import pandas as pd
from pathlib import Path


def load_country_data(data_dir: str = "data") -> pd.DataFrame:
    """Load all *_clean.csv files from `data_dir` and return a concatenated DataFrame.

    The function expects files named like `ethiopia_clean.csv`, `kenya_clean.csv`, etc.
    """
    p = Path(data_dir)
    files = list(p.glob("*_clean.csv"))
    dfs = []
    for f in files:
        df = pd.read_csv(f)
        df["source_file"] = f.name
        # attempt to parse time column
        if "time" in df.columns:
            df["time"] = pd.to_datetime(df["time"])
        dfs.append(df)
    if not dfs:
        return pd.DataFrame()
    return pd.concat(dfs, ignore_index=True)


def filter_by_country_and_year(df: pd.DataFrame, countries, year_range):
    if df.empty:
        return df
    res = df.copy()
    if countries:
        res = res[res["country"].isin(countries)]
    start, end = year_range
    if "time" in res.columns:
        res = res[(res["time"].dt.year >= start) & (res["time"].dt.year <= end)]
    return res
