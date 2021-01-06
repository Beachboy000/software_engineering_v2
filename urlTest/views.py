from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from account.mod import get_account
from django.contrib import messages
from room.mod import room
from seq.mod import seq
# Create your views here.


#打註解啦!!機掰人!!!


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
            messages.error(request, '輸入格式錯誤或用戶已存在 請重新輸入')
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

def goHistoryPage(request):
    if request.method == "POST":
        return render(request, 'history.html', locals())

def goHelpPage(request):
    if request.method == "POST":
        return render(request, 'help.html', locals())

def goReservePage(request):
    if request.method == "POST":
        return render(request, 'reservation.html', locals())

def borrow(request):
    if request.method == "POST":
        roomIn = request.POST['room_id']

        roomStr = roomIn            #字串轉換
        room_id = ''.join([x for x in roomStr if x.isdigit()])

        name = request.POST['userBorrow']
        start = request.POST['start_section']
        end = request.POST['end_section']
        population = request.POST['population']
        date = request.POST['date']
        purpose = request.POST['meeting_title']
        if room.check(room_id, start, end, date):
            room.reservation(room_id, start, end, date, purpose, name, population)
            messages.success(request, '成功預約~開心')
            return render(request, 'main.html', locals())

"""
def main(request):
    return render(request,'main.html',locals())
"""