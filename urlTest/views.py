from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from account.mod import get_account
from django.contrib import messages
#from django.template import loader
# Create your views here.

def loginPage(request):
    #return HttpResponse("FU")
    return render(request, 'login.html')
    #template=get_template('login.html')

def post(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        if get_account.getAccount(username, password):
            return render(request, 'main.html', locals())
        else:
            messages.error(request,'用戶名稱或密碼錯誤，ㄏㄏ')
            return redirect('/')
            #return redirect('/urlTest/loginPage/')
    else:
        mess = "Error"
    #return render(request, 'main.html', locals())

def goRegistPage(request):
    if request.method == "POST":
        return render(request, 'register.html', locals())

def regist(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        if get_account.register(username,password):
            messages.success(request, '成功註冊~開心')
            return redirect('/')
        else:
            messages.error(request, '用戶已存在，找茬嗎?')
            return redirect('/')

def goMainPage(request):
    if request.method == "POST":
        return render(request, 'main.html', locals())

def goOurInfoPage(request):
    if request.method == "POST":
        return render(request, 'ourInfo.html', locals())

def goDonatePage(request):
    if request.method == "POST":
        return render(request, 'donate.html', locals())

def goSearchPage(request):
    if request.method == "POST":
        return render(request, 'search.html', locals())
"""
def main(request):
    return render(request,'main.html',locals())
"""