import time
import requests
from datetime import datetime
import smtplib

# Variable for Latitude, longitude, email, password and start time
STARTTIME = time.time()
MY_LAT = 59.913868  # Your latitude
MY_LONG = 10.752245  # Your longitude
my_mail = "dennis.cardoso.122@gmail.com"
password = "ejtrsnsmkfqfgnor"


def iss_request():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_point = {
        "latitude": iss_latitude,
        "longitude": iss_longitude
    }

    return iss_point


def sunrise_sunset_request(parameters):
    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_point = {
        "sunrise": sunrise,
        "sunset": sunset
    }

    return time_point

# Your position is within +5 or -5 degrees of the ISS position.


while True:
    # get the ISS location
    iss_response = iss_request()

    # get the sunset and sunrise time
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    time_response = sunrise_sunset_request(parameters)

    # get the time and hour now
    time_now = datetime.now().time()
    hour_now = int(str(time_now).split(":")[0])

    # If the ISS is close to my current position
    if (-5 <= (MY_LAT - iss_response['latitude']) <= 5) and (-5 <= (MY_LONG - iss_response['longitude']) <= 5):
        iss_message = 'ISS is close of Dennis\'s position'
    else:
        iss_message = 'ISS is not close of Dennis\'s position'

    # and it is currently dark
    if (hour_now >= time_response['sunset'] and hour_now <= 23) or (hour_now >= 0 or hour_now <= time_response['sunrise']):
        is_dark = 'It is dark here'
    else:
        is_dark = 'It is not dark here'

# Then send me an email to tell me to look up.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs="dennis.cardoso@outlook.com", msg='Subject:ISS Dennis Position\n\nISS: {}\n\nDark:{}'.format(iss_message, is_dark))

# BONUS: run the code every 60 seconds.
time.sleep(60)
