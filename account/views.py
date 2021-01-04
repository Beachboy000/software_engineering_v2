from django.shortcuts import render
from .models import Account
from .mod import get_account
# Create your views here.

Account.objects.create(userName='B10730023@gmail.com',passWord = '12345678',userRoot = 'admin')

