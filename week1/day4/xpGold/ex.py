
def valid_int(self, val, excep):
    if not isinstance(val, int) or val < 0:
        raise Exception(f"Invalid {excep}")

class BankAccount:
    def __init__(self, balance, username, pw, auth=False):
        self.username = username
        self.pw = pw
        self.auth = auth
        self.balance = balance
        self.withdraw = None

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
        if self.curr_tries == self.try_limit:
            print("you exceeded your tries limit")
            return False
        else:
            login = input("Enter your Login : ")
            psw = input("Enter your Password : ")
            for obj in self.account_list:
                if obj.username == login and obj.pw == psw:
                    return True
            self.curr_tries += 1
            print("Error in login or Password")
            return False

    def show_main_menu(self):
        self.curr_tries = 0
        while 1:
            selection = input("1 - Log in | 2 - Exit : ")
            if selection == '2':
                exit("See you next time")
            if selection == '1':
                if self.logIn():
                    print("You loged in succesfully")













if __name__ == "__main__":
    pass