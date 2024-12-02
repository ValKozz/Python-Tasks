from django.db import models

# Create your models here.
class CityData(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    humidity = models.IntegerField()
    temp = models.DecimalField(decimal_places=2, max_digits=2)
    weather_desc = models.CharField(max_length=100)
    clouds = models.CharField(max_length=100)
    clouds_percent = models.IntegerField()