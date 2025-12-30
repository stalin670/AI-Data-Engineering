import petl as etl
import pandas as pd
import json

csv_data = etl.fromcsv('user_logs.csv')
json_data = etl.fromjson('api_metadata.json', lines=False)

csv_data = etl.convert(csv_data, 'user_id', int)
json_data = etl.convert(json_data, 'user_id', int)

integrated_table = etl.join(csv_data, json_data, key='user_id')

df = pd.DataFrame(etl.dicts(integrated_table))

# Fix timestamp parsing
df['timestamp'] = pd.to_datetime(
    df['timestamp'],
    dayfirst=True,
    errors='coerce'
)

# Fix list columns
for col in df.columns:
    if df[col].apply(lambda x: isinstance(x, list)).any():
        df[col] = df[col].apply(lambda x: json.dumps(x) if isinstance(x, list) else x)

# Drop duplicates safely
df = df.drop_duplicates(subset=['user_id', 'timestamp'])

# Fill NaNs safely
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].fillna(0)

print(df.head())
