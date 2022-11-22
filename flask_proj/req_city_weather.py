import requests
from typing import Dict
def get_weather(city='Minsk'):
    params={"q": city, 'appid': '65971f1eb2ea44d89056df3c182bc503', "units":'metric'}
    self_city_full=requests.get('https://api.openweathermap.org/data/2.5/weather', params=params).json()
   # print(self_city_full)
    self_city = {'city': city, 'main': self_city_full['main'], 'weather': self_city_full['weather'][0], 'wind': self_city_full['wind']}
    return self_city

print(get_weather())