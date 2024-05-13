import requests
from datetime import datetime
import time
import smtplib

# Change these constants to what suits you
MY_LAT = 31.985920  # Your latitude
MY_LONG = 35.897920  # Your longitude
MY_EMAIL = "example@gmail.com" # Your email
MY_PASSWORD = "yfsjiiwaawlgngfx" # Your password

# Getting ISS Information
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Parameters for the ISS API
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# getting the sunrise and sunset hours in my lat and lng
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# Get my personal hour
time_now = datetime.now().hour

# Setting up email message to send to my own email
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)

# Check if it's dark and ISS is close to my position
while True:
    time.sleep(60)
    if sunset_hour <= time_now <= sunrise_hour:
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
            # Send email to tell me to look up
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                msg="Subject:ISS is here!\n\nHey! Look up to the sky the ISS Should be above now!")
            