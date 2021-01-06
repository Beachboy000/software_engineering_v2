from seq.models import Seq
from room.models import Room
from room.models import Room
def detail(id,num):         #輸入detail進資料表
    Seq.objects.create(userName=id, user_run=num)

def userHistroy(id):            #用戶歷史
    status = Seq.objects.filter(userName=id)
    if status.exists():
        result = status.objects.order_by('-id')
        return result