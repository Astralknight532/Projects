# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:51:46 2022

@author: Frostmoon
"""

# Code to get weather info from the OpenWeather API 
# (requires use of the API key from their website) - need to login/signup and 
# use the default key (has to be activated from the website)
import requests # used for sending requests to websites
from pprint import pprint # pretty print

API_Key = '656168d0f479880e68755b5d2b67dd93'
city = input("Enter a city: ") # city you want weather info for
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid=' + API_Key + "&q=" + city
weather_data = requests.get(base_url).json() # get the data as JSON

# Print the weather data to console
pprint(weather_data)