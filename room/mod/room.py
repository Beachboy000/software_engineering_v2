from room.models import Room
from seq.models import Seq
import datetime

def check(id,start,end,date):       #檢查房間是否為空(輸入房間ID與時間)
    status = Room.objects.filter(roomID=id, date=date, start__gte=start, end__lte=end)
    if status.exists():
        return False
    else:
        return True

def getRoomStatus(id, date):
    status = Room.objects.filter(roomID=id, date=date)
    return status

def getHistory(date):             #獲得某天全部房間狀態
    status = Room.objects.filter(date=date).order_by('roomID')   # result為當天按照classID所排的list(僅傳被預約classID)
    return status

def reservation(id, start, end, date, purpose, username, num):   #預約前記得call check
      Room.objects.create(roomID=id, date=date, start=start, end=end, purpose=purpose)
      Seq.objects.create(roomID=id, date=date, start=start, end=end, userName=username)


'''
def check(id, start, end, date):       #檢查房間是否為空
    status = Room.objects.filter(roomID=id, start__range=(start, end), end__range=(start, end), date=date)
    if status.exists():
        return False
    else:
        return True

def getHistory(id):             #查詢歷史(by room)
    id = id
    status = Room.objects.filter(roomID = id)
    if status.exists():
        result = status.objects.order_by('start', 'end')
        return result

def reservation(id, start, end, date, purpose):     #預約前記得call check
      Room.objects.create(roomID=id, start=start, end=end, date=date, purpose=purpose)
'''


