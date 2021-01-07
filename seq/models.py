from django.db import models
from datetime import datetime
from datetime import date
# Create your models here.
class Seq(models.Model):
   #seq = models.IntegerField(default=0)
   '''
   userName = models.EmailField(unique=False)
   user_num = models.IntegerField()
   '''
   userName = models.EmailField(unique=False)
   user_num = models.IntegerField(default=0)
   roomID = models.IntegerField(unique=False, default=0)
   start = models.IntegerField(default=0)
   end = models.IntegerField(default=0)
   date = models.DateField(default=date.today())

