import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "" # insert your API key for Open Weather Map website
account_sid = "" # insert your Twilio Account ID
auth_token = "" # insert your Twilio Authorization token
# Amman lat long:
# "lat": 31.945368,
# "lon": 35.928371,
weather_params = {
    "lat": 31.945368,
    "lon": 35.928371,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# all list, list number (variable to loop on), weather list, weather number (variable to loop on), id
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for list in weather_data["list"]:
    for weather in list["weather"]:
        if weather["id"] < 700:
            will_rain = True

if will_rain is True:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an umbrella ☔"
             "\nOsama says hi :D",
        from_='+122xxxxxxx', # Add the phone number that's going to send the message
        to='+962xxxxxxx' # Add the phone number that will have the message sent to
    )
    print(message.status)
