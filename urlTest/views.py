from django.shortcuts import render,redirect
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
        username = request.POST['name']
        password = request.POST['password']
        if get_account.register(username, password):
            return render(request, 'main.html', locals())
        else :
            return redirect('/urlTest/showTemplate/')


    else:
        mess = "Error"
    #return render(request, 'main.html', locals())

def main(request):
    return render(request,'main.html',locals())
