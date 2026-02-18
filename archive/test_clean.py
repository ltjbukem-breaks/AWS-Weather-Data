import json
import boto3
import pandas as pd

s3 = boto3.client('s3')

# Specify your file
bucket = 'proj-weather-api'
key = 'raw/year=2026/month=02/day=16/weather_Goulding_Florida_20260216_050028.json'

# Read and process
response = s3.get_object(Bucket=bucket, Key=key)
data = json.loads(response['Body'].read().decode('utf-8'))

# Flatten and add metadata
df = pd.json_normalize(data['properties']['periods'])
df['city'] = data['city_metadata']['city']
df['state'] = data['city_metadata']['state']
df['latitude'] = data['city_metadata']['lat']
df['longitude'] = data['city_metadata']['lon']

print(df.head())
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nCity metadata: {df[['city', 'state', 'latitude', 'longitude']].iloc[0].to_dict()}")
