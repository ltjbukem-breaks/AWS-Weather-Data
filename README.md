# AWS-Weather-Data
This repo contains code used on an AWS free tier account to select a random city from uscities.csv and use it's longitude and latitude to retrieve weather data via [an API](https://api.weather.gov) based on a schedule, and to process it using AWS's cloud based DE tools.

Tools used: Eventbridge, S3, Lambda, Glue Crawler, Athena, IAM

Structure:

aws-weather-data-pipeline/
│
├── README.md
├── architecture-diagram.png
├── .gitignore
├── requirements.txt
│
├── lambdas/
│   ├── fetch_weather_data/ DONE
│   │   ├── lambda_function.py
│   │   └── README.md
│   │
│   ├── clean_weather_data/
│   │   ├── lambda_function.py
│   │   ├── README.md
│   │   └── test_event.json
│   │ 
│   └── layers/ DONE
│       └── README.md 
│
├── infrastructure/
│   ├── eventbridge-rule.json
│   ├── s3-event-notification.json
│   ├── iam-policies.json
│   └── glue-crawler-config.md
│
├── queries/
│   ├── average_temperature.sql
│   ├── daily_summary.sql
│   └── extreme_weather.sql
│
├── sample_data/ DONE
│   ├── raw_sample.json
│   └── cleaned_sample.json
│
└── weather-config/ DONE
    └── uscities.csv