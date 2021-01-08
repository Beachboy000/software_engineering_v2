from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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

def history(request):
    if request.method == "POST":
        #messages.error(request,'666')
        #userName = request.POST['userName']
        roomStr = request.POST['roomID']  # 字串轉換
        roomID = ''.join([x for x in roomStr if x.isdigit()])
        date = request.POST['date']

        if roomID !='':
            only_date = 0
            stat = room.getRoomStatus(roomID, date)
            return render(request, 'history.html', locals())
        else:
            only_date = 1
            stat = room.getHistory(date)
            return render(request, 'history.html', locals())

def goHelpPage(request):
    if request.method == "POST":
        return render(request, 'help.html', locals())

def search(request):
    '''
    if request.method == "POST":

        roomStr = request.POST['roomID']  # 字串轉換
        roomID = ''.join([x for x in roomStr if x.isdigit()])

        date = request.POST['date']
        stat = room.getRoomStatus(roomID, date)
        return render(request, 'search.html', locals())
    '''
    if request.method == "POST":
        roomStr = request.POST['roomID']  # 字串轉換
        roomID = ''.join([x for x in roomStr if x.isdigit()])

        date = request.POST['date']
        if roomID != '':
            is_only_date = 0
            stat = room.getRoomStatus(roomID, date)
            room1 = 0
            room2 = 0
            room3 = 0
            room4 = 0
            room5 = 0
            room6 = 0
            for i in stat:
                if i.roomID == 1:
                    room1 += 1
                elif i.roomID == 2:
                    room2 += 1
                elif i.roomID == 3:
                    room3 += 1
                elif i.roomID == 4:
                    room4 += 1
                elif i.roomID == 5:
                    room5 += 1
                elif i.roomID == 6:
                    room6 += 1

            occu1 = []
            occu2 = []
            occu3 = []
            occu4 = []
            occu5 = []
            occu6 = []

            occupied1 = []
            occupied2 = []
            occupied3 = []
            occupied4 = []
            occupied5 = []
            occupied6 = []

            for i in stat:
                if i.roomID == 1:
                    for j in range(i.start,i.end+1):
                        occu1.append(j)
                elif i.roomID == 2:
                    for j in range(i.start,i.end+1):
                        occu2.append(j)
                elif i.roomID == 3:
                    for j in range(i.start,i.end+1):
                        occu3.append(j)
                elif i.roomID == 4:
                    for j in range(i.start,i.end+1):
                        occu4.append(j)
                elif i.roomID == 5:
                    for j in range(i.start,i.end+1):
                        occu5.append(j)
                elif i.roomID == 6:
                    for j in range(i.start,i.end+1):
                        occu6.append(j)

            for i in range(1,11):
                if i not in occu1:
                    occupied1.append(0)
                else:
                    occupied1.append(1)
                if i not in occu2:
                    occupied2.append(0)
                else:
                    occupied2.append(1)
                if i not in occu3:
                    occupied3.append(0)
                else:
                    occupied3.append(1)
                if i not in occu4:
                    occupied4.append(0)
                else:
                    occupied4.append(1)
                if i not in occu5:
                    occupied5.append(0)
                else:
                    occupied5.append(1)
                if i not in occu6:
                    occupied6.append(0)
                else:
                    occupied6.append(1)




            return render(request, "search.html", locals())

        else:
            is_only_date = 1
            stat = room.getHistory(date)
            room1 = 0
            room2 = 0
            room3 = 0
            room4 = 0
            room5 = 0
            room6 = 0
            for i in stat:
                if i.roomID == 1:
                    room1 += 1
                elif i.roomID == 2:
                    room2 += 1
                elif i.roomID == 3:
                    room3 += 1
                elif i.roomID == 4:
                    room4 += 1
                elif i.roomID == 5:
                    room5 += 1
                elif i.roomID == 6:
                    room6 += 1

            occu1 = []
            occu2 = []
            occu3 = []
            occu4 = []
            occu5 = []
            occu6 = []

            occupied1 = []
            occupied2 = []
            occupied3 = []
            occupied4 = []
            occupied5 = []
            occupied6 = []

            for i in stat:
                if i.roomID == 1:
                    for j in range(i.start, i.end + 1):
                        occu1.append(j)
                elif i.roomID == 2:
                    for j in range(i.start, i.end + 1):
                        occu2.append(j)
                elif i.roomID == 3:
                    for j in range(i.start, i.end + 1):
                        occu3.append(j)
                elif i.roomID == 4:
                    for j in range(i.start, i.end + 1):
                        occu4.append(j)
                elif i.roomID == 5:
                    for j in range(i.start, i.end + 1):
                        occu5.append(j)
                elif i.roomID == 6:
                    for j in range(i.start, i.end + 1):
                        occu6.append(j)

            for i in range(1, 11):
                if i not in occu1:
                    occupied1.append(0)
                else:
                    occupied1.append(1)
                if i not in occu2:
                    occupied2.append(0)
                else:
                    occupied2.append(1)
                if i not in occu3:
                    occupied3.append(0)
                else:
                    occupied3.append(1)
                if i not in occu4:
                    occupied4.append(0)
                else:
                    occupied4.append(1)
                if i not in occu5:
                    occupied5.append(0)
                else:
                    occupied5.append(1)
                if i not in occu6:
                    occupied6.append(0)
                else:
                    occupied6.append(1)
            return render(request, "search.html", locals())


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
        if get_account.checkName(name):
            if room.check(room_id, start, end, date):
                room.reservation(room_id, start, end, date, purpose, name, population)
                messages.success(request, '成功預約~開心')
                return render(request, 'main.html', locals())
            else:
                messages.error(request, '本時段已有人預約...')
                return render(request, 'reservation.html', locals())
        else:
            messages.error(request, '帳號輸入錯誤 請重新輸入')
            return render(request, 'reservation.html', locals())


"""
def main(request):
    return render(request,'main.html',locals())
"""