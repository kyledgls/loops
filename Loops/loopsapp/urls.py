from django.conf.urls import url
from . import views

app_name = 'loopsapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getloop/$',views.getloop, name='getloop')
]
