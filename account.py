import random

class Account(object):

    def __init__(self, name , money):
        self.BANK = 'SC은행'  # 상수라서 대문자
        self.name = name
        self.account_number = self.create_account_number()
        self.money = money

    '''
       계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''

    def create_account_number(self):
        ls = []
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
                ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    def to_string(self):
        return f' Bank Bank:{self.BANK},'\
               f' Name:{self.name},'\
               f' Account_number:{self.account_number},'\
               f' Money:{self.money}'\

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        a = Account
        while 1:

            menu = input('0.Exit 1.Create 2.Read 3.Deposit 4.Withdraw 5.Delete')
            if menu == '0':
               # account = Account(None, None)
                break
            elif menu == '1':
                ls.append(a(input('name'),
                                  input('money')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())

            elif menu == '3':
                account_number = input('입금할 계좌번호')
                money = input('입금할 금액')
                if j.account_number == account_number:
                    replace = Account(j.account_number,
                                      j.name,
                                      int(j.money) + int(money))  # 입금 +
                    Account.del_account(ls, account_number)
                    ls.append(replace)

            elif menu == '4':
                account_number = input('출금할 계좌번호')
                money = input('출금액 입력바랍니다')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        replace = Account(j.account_number,
                                          j.name,
                                          int(j.money) - int(money))  # 출금 -
                        Account.del_account(ls, account_number)
                        ls.append(replace)

            elif menu == '5':
                Account.del_account(ls, input('삭제할 계좌번호'))

            else:
                print('Wrong number')
                continue

Account.main()
