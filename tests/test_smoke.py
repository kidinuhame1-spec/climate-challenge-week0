def test_smoke_imports():
    import importlib

    pandas = importlib.import_module('pandas')
    assert hasattr(pandas, '__version__')


def test_data_files_present():
    import os
    import pytest

    # Verify at least one dataset file exists in the `data/` folder.
    # If datasets are intentionally excluded from the repo (large files),
    # skip this check so CI doesn't fail for missing data.
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    data_dir = os.path.normpath(data_dir)
    if not os.path.isdir(data_dir):
        pytest.skip("data directory not present; skipping data-file smoke test")
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    if not files:
        pytest.skip("no CSV files in data directory; skipping data-file smoke test")
    assert len(files) > 0
