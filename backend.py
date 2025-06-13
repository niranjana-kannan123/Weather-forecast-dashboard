import requests
import os

api_key = os.getenv("PASSWORD")

def get_data(place, days, kind):
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    request = requests.get(url)
    content = request.json()

    if kind == "Temperature":
        temperature = []
        date = []
        for i in range(8*days):
            temperature.append(content["list"][i]["main"]["temp"]/10)
            date.append(content["list"][i]["dt_txt"])

        return temperature, date
    
    if kind == "Sky":
        sky = []
        date = []

        for i in range(8*days):
            sky.append(content["list"][i]["weather"][0]["main"])
            date.append(content["list"][i]["dt_txt"])

        return sky, date



