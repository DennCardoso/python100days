from typing import ParamSpec
import requests

MY_LAT = 59.913868
MY_LNG = 10.752245

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split(
    "T")[1].split(":")[0]  # .split("+")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[
    0]  # .split("+")[0]
print("Sunrise time: {}; Sunset time: {}".format(sunrise, sunset))


# If ISS is close to my current position
