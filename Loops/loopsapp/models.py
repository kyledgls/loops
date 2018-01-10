from django.db import models

# Create your models here




class SavedSearch(models.Model):
    email = models.CharField(max_length=250)
    name = models.CharField(max_length=20)
    json = models.TextField()
