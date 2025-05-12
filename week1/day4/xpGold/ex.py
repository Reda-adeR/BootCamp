
def valid_int(val, excep):
    if not isinstance(val, int) or val < 0:
        raise Exception(f"Invalid {excep}")

class BankAccount:
    def __init__(self, balance, username, pw, auth=False):
        self.username = username
        self.pw = pw
        self.auth = auth
        self.balance = balance

    def authenticate(self, userN, psw):
        if userN == self.username and psw == self.pw:
            self.auth = True
            return
        print("Credentials Incorrect !!")

    def isAuth(self):
        return self.auth

    def adDeposit(self, deposit):
        if not self.isAuth():
            raise Exception("Not Authenticated")
        valid_int(deposit, "deposit")
        self.balance += deposit
        print("added")

    def withdraw(self, val):
        if not self.isAuth():
            raise Exception("Not Authenticated")
        valid_int(val, "withdraw")
        self.balance -= val
        print("withdraw")




class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, username, pw, min_balance=0, auth=False):
        super().__init__(balance, username, pw, auth)
        self.minimum_balance = min_balance

    def withdraw(self, val):
        valid_int(val, "withdraw2")
        if self.balance - val < self.minimum_balance:
            raise Exception("Not enough Balance")
        else:
            self.balance -= val


class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list):
            raise Exception("Param passed is Not a list")
        for elem in account_list:
            if not isinstance(elem, BankAccount):
                raise Exception("List has unknown Object")
        self.account_list = account_list
        self.curr_tries = 0
        try:
            valid_int(try_limit, "Try Limit")
        except Exception:
            print("try Limit will be put to 2")
            self.try_limit = 2

    def logIn(self):
        if self.curr_tries == 3:
            print("you exceeded your tries limit")
            return False
        else:
            login = input("Enter your Login : ")
            psw = input("Enter your Password : ")
            for obj in self.account_list:
                if obj.username == login and obj.pw == psw:
                    obj.auth = True
                    return obj
            self.curr_tries += 1
            print("Error in login or Password")
            return False

    def withdraw(self, obj):
        val = input("enter Value of your withdraw : ")
        obj.withdraw(int(val))

    def deposit(self, obj):
        val = input("enter Value of your deposit : ")
        obj.adDeposit(int(val))

    def exit(self, obj):
        exit("Byeee", obj.username)

    def show_account_menu(self, obj):
        actionDict = {
            "1" : self.withdraw,
            "2" : self.deposit,
            "3" : self.exit          
        }
        while 1:
            print("before")
            selection = input("Choose an action : 1 - withdraw, 2 - deposit, 3 - exit")
            print("after")
            if selection not in actionDict:
                print("bad selection")
                continue
            actionDict[selection](obj)

    def show_main_menu(self):
        self.curr_tries = 0
        obj = None
        while 1:
            selection = input("1 - Log in | 2 - Exit : ")
            if selection == '2':
                exit("See you next time")
            if selection == '1':
                obj = self.logIn()
                if obj == False:
                    continue
                else:
                    print("You loged in succesfully")
                    break
        self.show_account_menu(obj)













if __name__ == "__main__":
    ac1 = BankAccount(100, "reda", "123", False)
    ac2 = BankAccount(500, "hamid", "321", True)
    ac3 = MinimumBalanceAccount(500, "hamid", "321", 200, True)
    gg = ATM([ac1, ac2, ac3], 3)
    gg.show_main_menu()