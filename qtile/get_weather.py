import requests, json

def get_weather():
    api_key = "711118f2be0b368b06fe7dc9f288a0b3"
    lat, lon= "40.73", "-73.93"
    base_url="https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}"
    units = "&units=imperial"
    complete_url = base_url.format(lat=lat, lon=lon, api_key=api_key) + units
    response = requests.get(complete_url)
    x = response.json()
    timezone = x['timezone'] 
    weather = x['current']['weather'][0]['main'] 
    temp = x['current']['temp']

    return timezone + ": " + weather + " " + str(temp) + "*"







