import os
os.environ['S3_BUCKET_NAME'] = 'proj-weather-api'
os.environ['CITIES_FILE'] = 'weather-config/uscities.csv'  # Path to CSV in S3

from lambda_ingest_weather import lambda_handler

# Test the function
event = {}
context = {}

try:
    result = lambda_handler(event, context)
    print("Success!")
    print(result)
except Exception as e:
    print(f"Error: {e}")