from django.shortcuts import render
from django.http import HttpResponse
from .secrets import google_maps_api_key

# Create your views here.
def index(request):
    print(google_maps_api_key)
    return render(request, 'loopsapp/index.html', {'google_maps_api_key':google_maps_api_key})


