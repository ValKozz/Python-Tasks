from . import models
from django.utils import timezone

def write(data):
	if type(data) == dict:
		last_city = list(models.CityData.objects.order_by("-pub_date"))[-1:]
		last_city[0].delete()

		models.CityData.objects.create(
			name = data['name'],
	    	country = data['country'],
	    	humidity = data['humidity'],
	    	temp = data['temp'],
	    	weather_desc = data['weather_desc'],
	    	clouds = data['clouds_percent'],
	    	clouds_percent= data['clouds_percent'],
	    	pub_date = timezone.now()
		    	)

	elif type(data) == list:
		last_five = list(models.CityData.objects.order_by("-pub_date"))[:5]
		for city in last_five:
			city.delete()

		for entry in data:		
			models.CityData.objects.create(
				name = entry['name'],
		    	country = entry['country'],
		    	humidity = entry['humidity'],
		    	temp = entry['temp'],
		    	weather_desc = entry['weather_desc'],
		    	clouds = entry['clouds'],
		    	clouds_percent= entry['clouds_percent'],
		    	pub_date = timezone.now()
		    	)