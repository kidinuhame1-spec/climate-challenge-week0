import pandas as pd
from pathlib import Path
import requests
import re
from io import BytesIO, StringIO


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
        # Ensure there's a `country` column. If missing, infer from filename
        # e.g. 'ethiopia_clean.csv' -> 'Ethiopia'
        if "country" not in df.columns:
            name = f.stem
            if name.endswith("_clean"):
                name = name[: -len("_clean")]
            country_name = name.replace("_", " ").replace("-", " ").title()
            df["country"] = country_name

        # attempt to parse or infer a time column
        # Accept common alternatives like 'date', 'datetime', 'timestamp'
        found_time_col = None
        for c in df.columns:
            if c.lower() in ("time", "date", "datetime", "timestamp", "time_utc", "time_local"):
                found_time_col = c
                break

        if found_time_col is not None:
            df["time"] = pd.to_datetime(df[found_time_col], errors="coerce")
        else:
            # Try to construct a datetime from year/month/day columns if present
            cols_lc = {col.lower(): col for col in df.columns}
            if "year" in cols_lc and "month" in cols_lc and ("day" in cols_lc or "day_of_month" in cols_lc):
                day_col = "day" if "day" in cols_lc else "day_of_month"
                try:
                    df["time"] = pd.to_datetime(
                        dict(
                            year=df[cols_lc["year"]].astype(int),
                            month=df[cols_lc["month"]].astype(int),
                            day=df[cols_lc[day_col]].astype(int),
                        ),
                        errors="coerce",
                    )
                except Exception:
                    pass

        dfs.append(df)
    if not dfs:
        return pd.DataFrame()
    return pd.concat(dfs, ignore_index=True)


def fetch_csv_from_url(url: str) -> pd.DataFrame:
    """Fetch a CSV from a public URL and return a pandas DataFrame.

    Handles Google Drive share links by converting them to a direct download URL.
    """
    if not url:
        raise ValueError("No URL provided")

    # Transform common Google Drive share URLs to direct-download form
    if "drive.google.com" in url:
        m = re.search(r"/d/([a-zA-Z0-9_-]+)", url)
        if not m:
            m = re.search(r"[?&]id=([a-zA-Z0-9_-]+)", url)
        if m:
            file_id = m.group(1)
            url = f"https://drive.google.com/uc?export=download&id={file_id}"

    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    # Try reading as bytes first, fall back to text
    data = resp.content
    try:
        return pd.read_csv(BytesIO(data))
    except Exception:
        try:
            return pd.read_csv(StringIO(data.decode("utf-8")))
        except Exception as e:
            raise ValueError(f"Could not parse CSV from URL: {e}")


def normalize_dataframe(df: pd.DataFrame, source_name: str | None = None) -> pd.DataFrame:
    """Normalize a loaded DataFrame to ensure `country` and `time` columns exist.

    - Infers `country` from `Country`, `country`, or `source_name`/filename.
    - Detects common time columns (`time`, `date`, `datetime`, `timestamp`) and parses them.
    - Attempts to build `time` from `YEAR`/`Month`/`Day` if present.
    Returns a copy of the DataFrame with `time` (datetime) and `country` populated where possible.
    """
    if df is None or df.empty:
        return df

    out = df.copy()

    # Country inference
    if "country" not in out.columns and "Country" in out.columns:
        out["country"] = out["Country"]

    if "country" not in out.columns and source_name:
        # infer from source_name (could be filename or URL)
        name = Path(source_name).stem
        if name.endswith("_clean"):
            name = name[: -len("_clean")]
        out["country"] = name.replace("_", " ").replace("-", " ").title()

    # Time detection
    found_time_col = None
    for c in out.columns:
        if c.lower() in ("time", "date", "datetime", "timestamp", "time_utc", "time_local"):
            found_time_col = c
            break

    if found_time_col is not None:
        out["time"] = pd.to_datetime(out[found_time_col], errors="coerce")
    else:
        cols_lc = {col.lower(): col for col in out.columns}
        # Accept YEAR/Month/Day variations
        if "year" in cols_lc and ("month" in cols_lc or "mon" in cols_lc) and (
            "day" in cols_lc or "doy" in cols_lc or "day_of_month" in cols_lc
        ):
            # prefer Month over mon, Day over doy/day_of_month
            month_col = cols_lc.get("month", cols_lc.get("mon"))
            day_col = cols_lc.get("day", cols_lc.get("day_of_month", cols_lc.get("doy")))
            try:
                out["time"] = pd.to_datetime(
                    dict(
                        year=out[cols_lc["year"]].astype(int),
                        month=out[month_col].astype(int),
                        day=out[day_col].astype(int),
                    ),
                    errors="coerce",
                )
            except Exception:
                pass

    return out


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
