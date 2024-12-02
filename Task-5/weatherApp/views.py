from django.shortcuts import render
from django.http import JsonResponse
from . import make_requests
from . import write_to_DB
from weatherApp.models import CityData
from django.core import serializers

import json

# Create your views here.
def index(request):
	return render(request, template_name="weatherApp/index.html") 

def getFive(request):
	amount = int(json.load(request))
	requester = make_requests.MakeRequests()

	# write to DB
	cities = requester.collect_cities(amount)
	write_to_DB.write(cities[0])

	json_data = json.dumps(cities)
# Sub-optimal but running out of time
	return JsonResponse(json_data, safe=False)

def getSingle(request):
	name = json.load(request)
	requester = make_requests.MakeRequests()

	# write to DB
	city = requester.get_by_name(name)
	write_to_DB.write(city)

	json_data = json.dumps(city)
# Sub-optimal but running out of time
	return JsonResponse(json_data, safe=False)

def getFromDB(request):
	pass
	json_data = serializers.serialize('json', CityData.objects.all())
	test = json.dumps(json_data)
	print(test)
	return JsonResponse(test, safe=False)
