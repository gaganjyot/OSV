from django.db import models

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='.')

class image_data(models.Model):
    image_path = models.CharField(max_length=200)
    location_x = models.FloatField()
    location_y = models.FloatField()
    approvals  = models.IntegerField()
