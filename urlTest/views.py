from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from account.mod import get_account
#from django.template import loader
# Create your views here.

def showTemplate(request):
    #return HttpResponse("FU")
    return render(request, 'login.html')
    #template=get_template('login.html')

def post(request):
    if request.method == 'POST':
        mess = request.POST['name']
        get_account.register(mess, '12345')
    else:
        mess = "Error"
    return render(request, 'main.html', locals())
