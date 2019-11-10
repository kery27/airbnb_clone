from django.db import models
from core import models as core_models
from django_countries.fields import CountryField

# Create your models here.


# class Room(models.Model):
class Room(core_models.TimeStampedModel):

    """Room Model Definition """

    name = models.TextField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
