from room.models import Room
import datetime

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


