from django.db import models

# Create your models here



class User(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.CharField(max_length=250)


class loop(models.Model):
    email = models.CharField(max_length=250)
    name_search = models.CharField(max_length=20)
    json = models.TextField()