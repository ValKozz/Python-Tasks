import requests
import os
from random import randrange

RAND_CITIES_AMOUNT = 5
LIMIT = 1
API_KEY = os.environ['API_KEY']
EXCLUDE_FROM_RESPONSE = "minutely,hourly,daily,alerts"
UNITS = "metric"

class MakeRequests():
    def __init__ (self):
        pass

    def get_data(self, latitude, longitude):
        city_lookup_raw = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&units={UNITS}&lon={longitude}&appid={API_KEY}")
        city_lookup_raw.raise_for_status()

        response = city_lookup_raw.json()
        return response


    def collect_cities(self):
        cities = []
        average_temp = 0
        while len(cities) < RAND_CITIES_AMOUNT:
            formated_city = self.get_random_city()
            cities.append(formated_city)

#         TODO - Fix this mess and return the needed values
        for formated_city in cities:
            average_temp += formated_city["temp"]
        average_temp = '{0:.2f}'.format(average_temp/RAND_CITIES_AMOUNT)

    #     min for each item in dict, item : item.temp
        min_temp_city = min(cities, key=lambda city:city["temp"])

        return {
            "data" : cities,
            "average_temp" : average_temp,
            "min" : min_temp_city["name"]
            }

    def format_data(self, city_data_full):
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

    def get_by_name(self, city_name):
        city_lookup_raw = requests.get (f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={LIMIT}&appid={API_KEY}")
        city_lookup_raw.raise_for_status()
        city_repsonse = city_lookup_raw.json()

        latitude = city_repsonse[0]["lat"]
        longitude = city_repsonse[0]["lon"]

        city_data_full = self.get_data(latitude, longitude)

        formated_data = format_data(city_data_full)
        return formated_data

    def get_random_city(self):
        longitude = randrange(-180, 181)
        latitude = randrange(-90, 91)
        city_data_full = self.get_data(latitude, longitude)

        # if the location is not actually a city, loop
        while not city_data_full["name"]:
            longitude = randrange(-180, 181)
            latitude = randrange(-90, 91)
            city_data_full = self.get_data(latitude, longitude)

        return self.format_data(city_data_full)


