from django.db import models

# Create your models here.
class Room(models.Model):
    roomID = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    seq = models.IntegerField()
