from django.shortcuts import render
from django.http import HttpResponse
from .secrets import google_maps_api_key
import json
import requests

# Create your views here.
def index(request):
    print(google_maps_api_key)
    return render(request, 'loopsapp/index.html', {'google_maps_api_key':google_maps_api_key})


def getloop(request):
    data = json.loads(request.body)
#    print(data['locations'])
    locations = data['locations']
    first = locations.pop(0)
    url = 'https://maps.googleapis.com/maps/api/directions/json?'
    url += 'key=' + google_maps_api_key
    url += '&origin=place_id:' + first
    url += '&destination=place_id:' + first
    url += '&waypoints=optimize:true|'
    for i in locations:
        url += 'place_id:' + i + '|'
    response = request.get(url)
    return HttpResponse(json.dumps(response))


    # return HttpResponse(json.dumps(data['locations']))



