from django.db import models

# Create your models here.
class Plant(models.Model):
    plant_name = models.CharField(max_length=264)
    plant_breed = models.CharField(max_length=264)
    time_created = models.DateTimeField()
    location = models.CharField(max_length=264)
    photo = models.ImageField(upload_to="photo")

    def __str__(self):
        return self.plant_namessss
    
