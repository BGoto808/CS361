##############################################################
# Weather_api.py: Program that allows the user to input a
#   location and obtains the current weather of that location 
#
# Author: Bryson Goto, 2/21/2022
##############################################################

# Importing libraries
import requests
from requests import get
import json, climage
import urllib.request
from PIL import Image

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

   # Getting the humidity
   humidity = main['humidity']

   # Getting the pressure
   pressure = main['pressure']

   # Printing weather information
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature} *F")
   print(f"Humidity: {humidity} %RH")
   print(f"Pressure: {pressure} kPa")
   print(f"Weather Report: {report[0]['description']}")

   # To Do: Implement microservice to return and print image of
   #     city, state, or country
   #urllib.request.urlretrieve(
   #'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Flag_of_Canada_%28Pantone%29.svg/800px-Flag_of_Canada_%28Pantone%29.svg.png',
   #'image.png')

   #img = Image.open('image.png');
   #img.show()

else:
   # Prints error message
   print("Error in the HTTP request")