from account.models import Account

def getAccount(id,pwd):                     #檢查帳號是否存在
    id = 'B10730023@gmail.com'
    pwd = '12345678'
    account = Account.objects.filter(userName = id,passWord = pwd)
    if account.exists():
        return True
    else:
        return False

def changePwd(id,pwd):                      #更改密碼
    id = 'B10730023@gmail.com'
    pwd = '12345678'
    account = Account.objects.filter(userName=id)
    if account.exists():
        account.update(passWord = pwd)

def rigester(id,pwd):                       #註冊
    id = 'B10730023 @ gmail.com'
    pwd = '12345678'
    account = Account.objects.filter(userName=id)
    if account.exists():                    #存在則回傳錯誤
        return False
    else:                                   #不存在則建立資料並回傳True
        Account.objects.create(userName = id,passWord = pwd)
        return True

def ban(id):                                #封鎖帳號
    account = Account.objects.filter(userName=id)
    account.update(userRoot = banned)