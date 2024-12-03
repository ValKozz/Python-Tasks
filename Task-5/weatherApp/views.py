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
	write_to_DB.write(cities[0], amount)

	json_data = json.dumps(cities)
# Sub-optimal but running out of time
	return JsonResponse(json_data, safe=False)

def getSingle(request):
	name = json.load(request)
	requester = make_requests.MakeRequests()

	# write to DB
	city = requester.get_by_name(name)
# Quick fix
	if city == "Error finding city, or invalid API response.":
		err = json.loads('{"err" : "Error finding city, or invalid API response."}')
		return JsonResponse(json.dumps(err), safe=False)

	write_to_DB.write(city)

	json_data = json.dumps(city)

# Sub-optimal but running out of time
	return JsonResponse(json_data, safe=False)

def getFromDB(request):
	json_data = json.loads(serializers.serialize('json', CityData.objects.all()))
	return JsonResponse(json_data, safe=False)
