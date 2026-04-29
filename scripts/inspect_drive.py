from app.utils import fetch_csv_from_url
import sys

url = 'https://drive.google.com/file/d/1Z8tkqUt3BTDqsstNBziA8Dp1_QWkFThc/view?usp=sharing'
print('Fetching', url)
try:
    df = fetch_csv_from_url(url)
except Exception as e:
    print('ERROR fetching CSV:', e)
    sys.exit(1)

print('COLUMNS:', list(df.columns))
print('\nSAMPLE:\n')
print(df.head(10).to_string(index=False))
