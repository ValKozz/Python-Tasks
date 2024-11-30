import requests
import os
from random import randrange

RAND_CITIES_AMOUNT = 5
LIMIT = 1
API_KEY = os.environ['API_KEY']
UNITS = "metric"

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

    formated_data = format_data(city_data_full)
    return print_city(formated_data)

def collect_cities():
    cities = []
    average_temp = 0
    while len(cities) < RAND_CITIES_AMOUNT:
        formated_city = get_random_city()
        cities.append(formated_city)
        print_city(formated_city)

    for formated_city in cities:
        average_temp += formated_city["temp"]
    print(f"Average temperature for all: {'{0:.2f}'.format(average_temp/RAND_CITIES_AMOUNT)}")
#     min for each item in dict, item : item.temp
    min_temp_city = min(cities, key=lambda city:city["temp"])
    print(f"Coldest city: {min_temp_city['name']}\n")

def get_random_city():
    longitude = randrange(-180, 181)
    latitude = randrange(-90, 91)
    city_data_full = get_data(latitude, longitude)

    # if the location is not actually a city, loop
    while not city_data_full["name"]:
        longitude = randrange(-180, 181)
        latitude = randrange(-90, 91)
        city_data_full = get_data(latitude, longitude)

    return format_data(city_data_full)

def format_data(city_data_full):
        formated_data ={
        "name": city_data_full["name"],
        "country": city_data_full["sys"]["country"],
        "humidity": city_data_full["main"]["humidity"],
        "temp": city_data_full["main"]["temp"],
        "weather_desc": city_data_full["weather"][0]["description"],
        "clouds": city_data_full["weather"][0]["main"],
        "clouds_percent": city_data_full["clouds"]["all"],
        }

        return formated_data

def print_city(formated_data):
    print(
f"""
Name: {formated_data["name"]}, {formated_data["country"]}
    Current Temperature: {formated_data["temp"]} C
    Humidity: {formated_data["humidity"]}%
    Clouds:  {formated_data["clouds_percent"]}% of sky covered by clouds
    Weather : {formated_data["clouds"]}
    Weather description: {formated_data["weather_desc"]}
""")


def main():
    option = input("City lookup (s)\nGet 5 random (r)\nQuit (q)\nPlease enter the desired option:\n")

    if option == "s".lower():
        name = input("City: ")
        get_by_name(name)
    elif option == "r".lower():
        collect_cities()
    elif option == "q".lower():
        quit()
    else:
        print("Invalid input. Try again\n")
        main()

if __name__ == '__main__':
    main()
