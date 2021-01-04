from django.db import models
from datetime import datetime
# Create your models here.
class Seq(models.Model):
   seq = models.IntegerField()
   userName = models.EmailField(blank=False,null=False,unique=True)
   user_run = models.IntegerField()
