import requests
from datetime import datetime
import smtplib
import time
MY_EMAIL= "deaf.defy@gmail.com"
MY_PASSWORD = "lrlw lzto kenk cdcb"
MY_LAT = 26.906010 # Your latitude
MY_LONG = 75.740730 # Your longitude
def iss_overheaed():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    
    if MY_LAT -5 < iss_latitude > MY_LAT +5 and MY_LONG- 5 < iss_longitude > MY_LONG + 5:
        return True
def nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_overheaed() and nighttime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="test383@myyahoo.com", msg="Subject: ISS Within your area!\n\nThere is ISS wandering around your area.")




