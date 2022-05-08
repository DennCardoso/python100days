import requests

weather_endpoint = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 59.917180,
    "lon": 10.695490,
    "appid": "228b2c371fca593249846b5f5d78b1e2",
}

response = requests.get(weather_endpoint, params=weather_params)
response.raise_for_status()
print(response.json())
