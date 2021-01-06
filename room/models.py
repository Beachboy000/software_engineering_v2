from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    roomID = models.IntegerField(unique=True)
    '''
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    '''
    date=models.DateTimeField(default=datetime.now())
    classID=models.IntegerField(default=0)
    seq = models.IntegerField()
