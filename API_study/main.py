import requests
from datetime import datetime

time_now = datetime.now()
time_now = time_now.hour
print(time_now)


MY_LAT = -22.9110137
MY_LNG = -43.2093727

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunset = str(data["results"]["sunset"]).split("T")[1].split(":")[0]
sunrise = str(data["results"]["sunrise"]).split("T")[1].split(":")[0]
print(sunset)
print(sunrise)
