import os

import requests
from datetime import datetime
import smtplib
import time
from dotenv import load_dotenv
load_dotenv(override=True)

MY_LAT = 35.496456 # Your latitude
MY_LNG = -83.450469 # Your longitude
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
SEND_TO = os.getenv("SEND_TO")

def is_iss_overhead():
    # Location of International Space Station
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    # My position is within +5 or -5 degrees of the ISS position.
    if abs(MY_LAT - iss_lat) <= 5 and abs(MY_LNG - iss_lng) <= 5:
        return True

def set_hour(hour, minute):
    if minute > 30:
        hour += 1
    return hour


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid": "America/New_York"
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    suntimes_data = response.json()

    sunrise = set_hour(int(suntimes_data["results"]["sunrise"].split("T")[1].split(":")[0]),
                       int(suntimes_data["results"]["sunrise"].split("T")[1].split(":")[1]))

    sunset = set_hour(int(suntimes_data["results"]["sunset"].split("T")[1].split(":")[0]),
                      int(suntimes_data["results"]["sunset"].split("T")[1].split(":")[1]))

    time_now = set_hour(datetime.now().hour, datetime.now().minute)
    if time_now >= sunset or time_now <= sunrise:
            return True
    return False

while True:
    time.sleep(300)
    if is_iss_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=SEND_TO,
                                    msg=f"Subject: International Space Station is overhead!\n\n"
                                        f"Go outside and look up to see the International Space Station!")