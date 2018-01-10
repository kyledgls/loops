from django.conf.urls import url
from . import views
import requests

app_name = 'loopsapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^loginu/$', views.loginu, name='loginu'),
    url(r'^logoutu/$', views.logoutu, name='logoutu'),
    url(r'^save_search/$', views.save_search, name='save_search')
    
]
