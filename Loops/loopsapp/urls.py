from django.conf.urls import url
from . import views
import requests

app_name = 'loopsapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getloop/$',views.getloop, name='getloop'),
    url(r'^loginpanel/$', views.loginpanel, name='loginpanel'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^loginu/$', views.loginu, name='loginu')

]
