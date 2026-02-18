# Script Name: ingest_weather.py
# Description: Ingests weather data via an API from NOAA (https://www.weather.gov/documentation/services-web-api)
# Author: Alistair A.

import pandas as pd
import requests
import json

# Read in list of US cities csv
fp_us_cities = "C:/Users/aches/Desktop/Stuff/VSCode/AWS-Weather-Data/weather-config/uscities.csv"
df_us_cities = pd.read_csv(fp_us_cities)

# Test retrieve from API
test_url = "https://api.weather.gov/points/38.8894,-77.0352"

response_API = requests.get(test_url)
data = response_API.text
parsed_data = json.loads(data)
parsed_data.keys()
parsed_data['properties']['forecast']

# Pull the URL from the properties/forecast json
forecast_url = parsed_data['properties']['forecast']
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.text
forecast_parsed_data = json.loads(forecast_data)

# Convert to pd.DataFrame
df = pd.json_normalize(forecast_parsed_data)
df.columns

forecast_parsed_data['properties']['periods'] # This has each day of the week

# Saving as .JSON for easier viewing
"""
with open("weather.json", "w", encoding="utf-8") as f:
    json.dump(forecast_parsed_data, f)
"""

# Testing converting the weekly forecast into a pd.dataframe
# Still has some sublists but can at least store this as S3, then clean up in Glue
df_periods = pd.DataFrame(forecast_parsed_data['properties']['periods'])
df_periods.columns
"""
Index(['number', 'name', 'startTime', 'endTime', 'isDaytime', 'temperature',
       'temperatureUnit', 'temperatureTrend', 'probabilityOfPrecipitation',
       'windSpeed', 'windDirection', 'icon', 'shortForecast',
       'detailedForecast'], 
"""


"""
GENERAL OUTLINE FOR LAMBDA FILE
   ├── Read cities.csv from S3
   ├── Randomly select 5 cities
   ├── Call weather API for each
   └── Write 5 raw JSON files to S3
"""

def fetch_city_lan_lon(n): 
    """Pulls latitude and longitude for n randomly picked cities in the US
       Returns as pd.DataFrame

    Args:
        n (int): number of randomly picked cities
    """
    fp_us_cities = "C:/Users/aches/Desktop/Stuff/VSCode/AWS-Weather-Data/weather-config/uscities.csv"
    df_us_cities = pd.read_csv(fp_us_cities)

    return df_us_cities.sample(n)[["city", "state_name", "lat", "lng", "population", "timezone"]]
