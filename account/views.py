from django.shortcuts import render
from .models import Account
# Create your views here.

Account.objects.create(userName='B10730023@gmail.com',passWord = '12345678',userRoot = 'admin')

