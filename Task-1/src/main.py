import requests
import os
from random import randrange

RAND_CITIES = 5
LIMIT = 1
API_KEY = os.environ['API_KEY']
EXCLUDE_FROM_RESPONSE = "minutely,hourly,daily,alerts"
UNITS = "metric"


def get_random_city():
    longitude = randrange(-180, 181)
    latitude = randrange(-90, 91)
    city_data_full = get_data(latitude, longitude)

    # if the location is not actually a city, loop
    while not city_data_full["name"]:
        longitude = randrange(-180, 181)
        latitude = randrange(-90, 91)
        city_data_full = get_data(latitude, longitude)

    return format_and_print(city_data_full)


def format_and_print(city_data_full):
        name = city_data_full["name"]
        country = city_data_full["sys"]["country"]
        humidity = city_data_full["main"]["humidity"]
        temp = city_data_full["main"]["temp"],
        weather_desc = city_data_full["weather"][0]["description"]
        clouds = city_data_full["weather"][0]["main"]
        clouds_percent = city_data_full["clouds"]["all"]

        format_print =\
f"""
Name: {name}, {country}
    Current Temperature: {temp} C
    Humidity: {humidity}%
    Clouds:  {clouds_percent}% of sky covered by clouds
    Weather : {clouds}
    Weather description: {weather_desc}
"""
        print(format_print)

def get_data(latitude, longitude):
    city_lookup_raw = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&units={UNITS}&lon={longitude}&appid={API_KEY}")
    city_lookup_raw.raise_for_status()

    response = city_lookup_raw.json()
    return response

def get_by_name(city_name):
    city_lookup_raw = requests.get (f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={LIMIT}&appid={API_KEY}")
    city_lookup_raw.raise_for_status()
    city_repsonse = city_lookup_raw.json()

    latitude = city_repsonse[0]["lat"]
    longitude = city_repsonse[0]["lon"]

    city_data_full = get_data(latitude, longitude)

    return format_and_print(city_data_full)

def main():
    option = input("City lookup (s)\nGet 5 random (r)\nQuit (q)\nPlease enter the desired option:\n")

    if option == "s".lower():
        name = input("City: ")
        get_by_name(name)
    elif option == "r".lower():
        for i in range (0, 5):
            get_random_city()
    elif option == "q".lower():
        quit()
    else:
        print("Invalid input. Try again\n")
        main()

if __name__ == '__main__':
    main()
