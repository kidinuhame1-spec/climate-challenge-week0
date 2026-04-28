def test_smoke_imports():
    import importlib

    pandas = importlib.import_module('pandas')
    assert hasattr(pandas, '__version__')


def test_data_files_present():
    import os

    # Verify at least one dataset file exists in the `data/` folder.
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    data_dir = os.path.normpath(data_dir)
    assert os.path.isdir(data_dir)
    files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    assert len(files) > 0
