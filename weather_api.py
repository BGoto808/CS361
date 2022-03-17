##############################################################
# Weather_api.py: Program that allows the user to input a
#   location and obtains the current weather of that location 
#   Uses wiki image scrapper microservice to display the image
#   of that city
#
# Author: Bryson Goto, 2/27/2022
##############################################################

import requests
from requests import get
import json, climage
import urllib.request
from PIL import Image
import subprocess
import scrape_image 

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# User inputs a city
CITY = input("Enter a location: ")

# API key for WeatherMap
API_KEY = "9fe048215c91d6c4f2f280b4e0b8cb5c"

# Updating the URL to connect to
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# HTTP request
response = requests.get(URL)

# Checking the status code of the request
if response.status_code == 200:
   # Formatting data into json
   data = response.json()

   # Getting main dictionary
   main = data['main']

   # Getting temperature and converting from Kelvin to Fahrenheit
   temperature = main['temp']
   temperature = int(temperature * 1.8 - 459.67)

   # Getting the humidity and pressure
   humidity = main['humidity']
   pressure = main['pressure']

   # Printing weather information
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature} *F")
   print(f"Humidity: {humidity} %RH")
   print(f"Pressure: {pressure} kPa")
   print(f"Weather Report: {report[0]['description']}")

   # Gets image of city and displays it using microservice
   # Make request to API endpiont
   response = get(
      url="http://flip1.engr.oregonstate.edu:1876/" + CITY
   )

   # Convert response to dict object
   response = response.json()

   # Get URL item
   response_url = response["url"]

   urllib.request.urlretrieve(
      response_url,
      'image.png')

   img = Image.open('image.png');
   img.show()

else:
   # Prints error message
   print("Error in the HTTP request")