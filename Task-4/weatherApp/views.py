from django.shortcuts import render
from django.http import JsonResponse
from . import make_requests
import json

# Create your views here.
def index(request):
	return render(request, template_name="weatherApp/index.html")

def getFive(request):
	amount = int(json.load(request))
	requester = make_requests.MakeRequests()
	json_data = json.dumps(requester.collect_cities(amount))
# Sub-optimal but running out of time
	return JsonResponse(json_data, safe=False)

def getSingle(request):
	passS