from room.models import Room
import datetime

def check(id,start,end):       #檢查房間是否為空
    id = 1
    start = datetime.datetime(2021,1,1,12,0)
    end = datetime.datetime(2021,1,1,14,0)
    status = Room.objects.filter(roomID=id, start_time__range=(start, end), end_time__range=(start, end))
    if status.exists():
        return False
    else:
        return True

    '''
     status = Room.objects.filter(roomID=id, start_time__range=(start, end), end_time__range=(start, end))
    if status.exists():
        return False
    else:
        return True
    '''

def getHistory(id):             #查詢歷史(by room)
    id = 1
    status = Room.objects.filter(roomID = id)
    if status.exists():
        result = status.objects.order_by('start_time','end_time')
        return result
    '''
    status = Room.objects.filter(roomID = id)
    if status.exists():
        result = status.objects.order_by('start_time','end_time')
        return result
    '''
def reservation(id,start,end):     #預約
    if(check(id,start,end)):
      Room.objects.create(roomID = id,start_time = start,end_time = end)
      return True
    else:
      return False
