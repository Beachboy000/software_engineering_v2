from django.db import models
from datetime import datetime
from datetime import date
# Create your models here.
class Room(models.Model):
    roomID = models.IntegerField(unique=False)
    '''
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date = models.DateTimeField(default=datetime.now())
    '''
    seq = models.IntegerField(default=0)
    start = models.IntegerField(default=0)
    end = models.IntegerField(default=0)
    date = models.DateField(default=date.today())
    purpose = models.CharField(max_length=10, default='')