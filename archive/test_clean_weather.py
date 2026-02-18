# test_clean_weather.py
from cleanWeatherData import lambda_handler

# Mock S3 event
event = {
    'Records': [{
        's3': {
            'bucket': {'name': 'proj-weather-api'},
            'object': {'key': 'raw/year=2026/month=02/day=15/weather_Chapin_Illinois_20260215_194540.json'}
        }
    }]
}

context = {}

result = lambda_handler(event, context)
print(result)
