import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 45.454410
MY_LONG = -75.484990
MY_EMAIL = "sterous@gmail.com"
RECEIVER_EMAIL = "steve.rousseau@bell.net"
MY_PASSWORD = "jekraqeyxlyhfnwr"


def is_iss_overhaad():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude)
    print(iss_latitude)
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 4
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 4

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhaad() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            # makes connection secure
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECEIVER_EMAIL,
                                msg=f"Subject:ISS Position!\n\nThe ISS should be visible in the sky.  Go take a look"
            )