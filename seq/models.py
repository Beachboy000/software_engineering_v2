from django.db import models
from datetime import datetime
# Create your models here.
class Seq(models.Model):
   #seq = models.IntegerField(default=0)
   userName = models.EmailField(unique=False)
   user_num = models.IntegerField()
