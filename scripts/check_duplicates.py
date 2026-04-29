import pandas as pd
from pathlib import Path
import hashlib

p = Path('data')
rows = []
files = list(p.glob('*.csv'))
for f in files:
    df = pd.read_csv(f)
    n = len(df)
    nunique = len(df.drop_duplicates())
    dup_rows = n - nunique
    # file hash
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    rows.append({'file': f.name, 'rows': n, 'unique_rows': nunique, 'dup_rows': dup_rows, 'hash': h})

print('File summary:')
for r in rows:
    print(f"{r['file']}: rows={r['rows']}, unique={r['unique_rows']}, dup_rows={r['dup_rows']}")

# find identical files by hash
from collections import defaultdict
byhash = defaultdict(list)
for r in rows:
    byhash[r['hash']].append(r['file'])

print('\nIdentical files:')
for h, fl in byhash.items():
    if len(fl) > 1:
        print(fl)

# summary totals
total_rows = sum(r['rows'] for r in rows)
total_dup = sum(r['dup_rows'] for r in rows)
print(f"\nTotal rows: {total_rows}, total duplicate rows (per-file): {total_dup}")
