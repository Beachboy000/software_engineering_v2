from account.models import Account
import re

regex = '^[A-z0-9]+[\._]?[a-z0-9]+@(\w+.)+(com|tw)$'    #email格式

def getAccount(id,pwd):                     #檢查帳號是否存在(登入用)
    '''
    idTest = 'B10730023@gmail.com'
    pwdTest = '12345678'
    '''

    account = Account.objects.filter(userName=id, passWord=pwd)
    if account.exists():
        return True
    else:
        return False

def checkName(id):
    account = Account.objects.filter(userName=id)
    if account.exists():
        return True
    else:
        return False

def changePwd(id,pwd):                      #更改密碼
    '''
    idTest = 'B10730023@gmail.com'
    pwdTest = '12345678'
    account = Account.objects.filter(userName=idTest)
    if account.exists():
        account.update(passWord = pwdTest)
    '''

    account = Account.objects.filter(userName=id)
    if account.exists():
        account.update(passWord=pwd)



def register(id,pwd):                       #註冊
    '''
    idTest = 'B10730023 @ gmail.com'
    pwdTest = '12345678'
    account = Account.objects.filter(userName=idTest)
    if account.exists():                    #存在則回傳錯誤
        return False
    else:                                   #不存在則建立資料並回傳True
        Account.objects.create(userName = idTest,passWord = pwdTest)
        return True
    '''

    account = Account.objects.filter(userName=id)
    if (re.search(regex,id)):
        if account.exists():
            return False
        else:
            Account.objects.create(userName=id, passWord=pwd)
            return True
    else:
        return False




def ban(id):                                #封鎖帳號
    account = Account.objects.filter(userName=id)
    account.update(userRoot = 'banned')