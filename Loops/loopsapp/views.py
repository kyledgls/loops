from django.shortcuts import render
from django.http import HttpResponse
from .secrets import google_maps_api_key
import json

# Create your views here.
def index(request):
    print(google_maps_api_key)
    return render(request, 'loopsapp/index.html', {'google_maps_api_key':google_maps_api_key})

def getloop(request):
    data = json.loads(request.body)
    print(data['locations'])


    return HttpResponse('test123')


