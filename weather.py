#!/usr/bin/env python3

import requests, sys

#Determining location based on command lines arguments.
if len(sys.argv) < 2:
    print('Usage: weather.py location')
    sys.exit()
location = ''.join(sys.argv[1:])
api_key = 'YOUR_API_KEY'

#Downloading data from the OpenWeatherMap.org API.
url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&cnt=3&appid={api_key}&units=metric'
response = requests.get(url)
response.raise_for_status()

#Displaying a description of the weather forecast.
weatherData = response.json()
print(f'Weather for: {weatherData['name']}')
print(weatherData['weather'][0]['main'], '-', weatherData['weather'][0]['description'])
print(f'Temperature: {weatherData['main']['temp']}°C')