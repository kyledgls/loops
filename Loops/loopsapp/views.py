from django.shortcuts import render
from django.http import HttpResponse
from .secrets import google_maps_api_key
import json
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    isLoggedIn = request.user.is_authenticated
    return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': isLoggedIn})


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
    print(url)
    response = requests.get(url)
    return HttpResponse(json.dumps(response.json()))


    # return HttpResponse(json.dumps(data['locations']))


def loginpanel(request):
    print('loginpanel is reached')
    if request.user.is_authenticated:
        return HttpResponse('you are logged in')
    else:
        return HttpResponse('You are not logged in')

def signup(request):
    email = request.POST['ename']
    first = request.POST['fname']
    last = request.POST['lname']
    password = request.POST['password']
    user = User.objects.create_user(email, email=email, password=password)
    user.first_name = first
    user.last_name = last
    user.save()
    return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': True})

def loginu(request):

    email = request.POST['ename']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    print(user)
    if user is not None:
        return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': True})


