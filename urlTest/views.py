from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showTemplate(request):
    #return HttpResponse("FU")
    return render(request,'test.html')