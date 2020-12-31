from django.db import models

# Create your models here.
class Seq(models.Model):
   seq = models.IntegerField()
   userName = models.CharField(max_length=50)
   user_run = models.IntegerField()
