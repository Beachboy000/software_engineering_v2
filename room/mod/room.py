from room.models import Room
from seq.models import Seq
import datetime

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


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
      mail(id, start, end, date, purpose, username, num)


def mail(id, start, end, rdate, purpose, username, num):
    chrome_options = Options()
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    chrome_options.add_argument("user-agent={}".format(useragent))

    chrome_options.add_argument('--headless')

    # 開啟瀏覽器視窗(Chrome)
    # 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("https://calendar.google.com/")

    driver.implicitly_wait(50)

    # 帳號
    account = driver.find_element_by_css_selector("#identifierId")
    account.send_keys("B10730023@gapps.ntust.edu.tw")
    send_account = driver.find_element_by_css_selector("#identifierNext > div > button > div.VfPpkd-RLmnJb")
    send_account.click()
    # 密碼
    element = driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    element.send_keys("William0857")
    button = driver.find_element_by_css_selector('#passwordNext > div > button > div.VfPpkd-RLmnJb')
    button.click()

    # button = driver.find_element_by_css_selector('#yDmH0d > div > div > div.I7OXgf.t6NDEb.ZEeHrd.Inn9w.iWO5td > div.OE6hId.J9fJmf > div:nth-child(3) > span > span')
    # button.click()
    # 建立活動
    button = driver.find_element_by_css_selector(
        "body > div.tEhMVd > div.pSp5K > div.KKOvEb > div.dwlvNd > button > span.VfPpkd-Q0XOV")
    button.click()
    # 標題
    title = driver.find_element_by_css_selector(
        "#yDmH0d > div > div > div.RDlrG.Inn9w.iWO5td > span > div > div.q2nced > div.K0f0Xc.cyTuMc > div.ZX9XLb > div.mvRfff > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    title.send_keys("空間借用通知信--(地點 : " + str(id) + ")")

    # 更多選項
    button = driver.find_element_by_css_selector(
        "#yDmH0d > div > div > div.RDlrG.Inn9w.iWO5td > span > div > div.q2nced > div.K0f0Xc > div.BTotkb.JaKw1 > div.uArJ5e.UQuaGc.kCyAyd.nYqxP > span > span")
    button.click()
    # 全天
    button = driver.find_element_by_css_selector("#xAlDaCbx > div.uHMk6b.fsHoPb")
    button.click()
    sleep(3)

    # 時間更改!!!!!!

    # driver.find_element_by_css_selector("#xStDaIn").clear()
    date = driver.find_element_by_css_selector("#xStDaIn")
    date.click()
    sleep(1)
    date.send_keys(Keys.BACKSPACE)
    date.clear()
    date.send_keys(str(rdate))
    # time.sleep(2)

    # 主體
    content = driver.find_element_by_css_selector("#T2Ybvb2")
    content.send_keys("申請目的 : "+purpose+"\n"
                      "地點 : "+str(id)+"\n"
                      "借用日期 : "+str(rdate)+"\n"
                      "借用人 : "+username+"\n"
                      "人數 : "+str(num)+"\n"
                      "申請時段 : "+str(start)+" ~ "+str(end)+"\n"
                      "◎此信件為系統發出信件，請勿直接回覆\n")

    invite = driver.find_element_by_css_selector(
        "#tabGuests > div.YxiWic.mCosT > div > span > div > div.d1dlne.WvJxMd > div.rFrNMe.Ax4B8.ULpymb.zKHdkd.Tyc9J > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
    invite.send_keys(str(username))

    # 送出
    button = driver.find_element_by_css_selector("#xSaveBu > span")
    button.click()
    button = driver.find_element_by_css_selector(
        "#yDmH0d > div > div > div.I7OXgf.dT3uCc.gF3fI.fNxzgd.Inn9w.iWO5td > div.OE6hId.J9fJmf > div > div.uArJ5e.UQuaGc.kCyAyd.l3F1ye.ARrCac.HvOprf.fY7wqd.M9Bg4d > span > span")
    button.click()
    button = driver.find_element_by_css_selector(
        "#yDmH0d > div > div > div.I7OXgf.dT3uCc.gF3fI.fNxzgd.Inn9w.iWO5td > div.OE6hId.J9fJmf > div > div.uArJ5e.UQuaGc.kCyAyd.l3F1ye.ARrCac.HvOprf.evJWRb.M9Bg4d > span > span")
    button.click()

    time.sleep(10)
    driver.close()


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


