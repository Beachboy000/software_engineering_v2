from account.models import Account

#from account.mod.get_account import accountSet
class accountSet(Account):
    def getAccount(id, passW):                     #檢查帳號是否存在
        '''
        getName = 'example@gmail.com'
        getPass = '1234'
        '''
        account = Account.objects.filter(userName=id, passWord=passW)
        if account.exists():
            return True
        else:
            return False

    def changePwd(id,newPass):                      #更改密碼
        '''
        changeName = 'example@gmail.com'
        passW = '12345'
        '''
        account = Account.objects.filter(userName=id)
        if account.exists():
            account.update(passWord = newPass)

    def register(id,passW):                       #註冊
        '''
        reName = 'example@gmail.com'              #form = 'example@gmail.com'
        rePass = '1234'
        '''
        account = Account.objects.filter(userName=id)
        if account.exists():                    #存在則回傳錯誤
            return False
        else:                                   #不存在則建立資料並回傳True
            Account.objects.create(userName = id,passWord = passW)
            return True