from nbconvert import HTMLExporter
import nbformat
from pathlib import Path
nb_path = Path('notebooks/compare_countries.ipynb')
out_path = Path('notebooks/compare_countries.html')
nb = nbformat.read(nb_path, as_version=4)
exporter = HTMLExporter()
body, resources = exporter.from_notebook_node(nb)
out_path.write_text(body, encoding='utf-8')
print(f'Wrote {out_path}')
