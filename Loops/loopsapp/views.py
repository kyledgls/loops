from django.shortcuts import render
from django.http import HttpResponse
from .secrets import google_maps_api_key
import json
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from loopsapp.models import SavedSearch

# Create your views here.
def index(request):
    isLoggedIn = request.user.is_authenticated
    if isLoggedIn:
      return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': True, 'first': request.user.first_name, 'ss':get_saved_searches(request.user.get_username())})
    else:
      return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': False})


def signup(request):
    email = request.POST['ename']
    first = request.POST['fname']
    last = request.POST['lname']
    password = request.POST['password']
    user = User.objects.create_user(email, email=email, password=password)
    user.first_name = first
    user.last_name = last
    user.save()
    return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': True,'first': request.user.first_name, 'ss':get_saved_searches(email)})

def loginu(request):

    email = request.POST['ename']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    print(user)
    if user is not None:
        return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': True,'first': user.first_name, 'ss': get_saved_searches(email)})

def logoutu(request):
    logout(request)
    return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': False})

def get_saved_searches(email):
    match = []
    sso = SavedSearch.objects.all()
    for s in sso:
      print(s.get_email())
      if s.email == email:
        match.append(s)
    return match

def save_search(request):
    email = request.user.get_username()
    name = request.POST['search_name']
    json = request.POST['json_hidden']
    ss = SavedSearch(email=email, name=name, json=json)
    ss.save()
    #user = User.objects.get(username=email)
    return render(request, 'loopsapp/index.html', {'google_maps_api_key': google_maps_api_key, 'loggedin': True,'first': email,  'ss': get_saved_searches(email)})

