from django.db import models

# Create your models here.
class CityData(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    humidity = models.IntegerField()
    temp = models.FloatField()
    weather_desc = models.CharField(max_length=100)
    clouds = models.CharField(max_length=100)
    clouds_percent = models.IntegerField()
    # Used to order and delete the oldest
    pub_date = models.DateTimeField("date published")

    def __str__(self):
    	return self.name

    class Meta:
       ordering = ['-pub_date']