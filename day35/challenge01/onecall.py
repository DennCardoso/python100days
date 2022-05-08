import requests

weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"

weather_params = {
    "lat": 59.917180,
    "lon": 10.695490,
    "appid": "228b2c371fca593249846b5f5d78b1e2",
}

response = requests.get(weather_endpoint, params=weather_params)
onecall = response.json()
# print the response status
print('http response status: {}'.format(response))

# Print the response to the console
print('json response: {}\n'.format(onecall))
# print(response.raise_for_status())
# print('http response status: {}'.format(response.status_code))
# print(response.json())

