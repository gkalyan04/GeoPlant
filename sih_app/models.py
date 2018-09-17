from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.
class Plant(models.Model):
    plant_name = models.CharField(max_length=264)
    plant_breed = models.CharField(max_length=264)
    location = GeopositionField()
    photo = models.ImageField()

    def __str__(self):
        return self.plant_name
    
