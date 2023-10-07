from django.db import models
from django.contrib.auth.models import AbstractUser
# This is a table for the data base
class User (AbstractUser):
    pass 
# name of plant, description, price, image, region, 
class Plant (models.Model):
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length= 500)
    price = models.FloatField()
    image = models.CharField(max_length= 500)
    region = models.CharField(max_length= 50)
    