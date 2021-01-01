from django.db import models

# Create your models here.
class Account(models.Model):
    userName = models.EmailField(blank=False,null=False,unique=True)
    passWord = models.CharField(max_length=30)
    userRoot = models.CharField(default= "unrooted",max_length=10)