class Bank:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.__account_number = account_number

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed")

    def __internal_method(self):
        print("Private Method")
        print(self.__account_number)
        print(self.balance)


hdfc = Bank(9876543210, 100)
hdfc.deposit(300)
print(hdfc.balance)
hdfc.check_balance()
hdfc.show_me_account_number(True)
hdfc.show_me_account_number(False)
# hdfc.__internal_method() - Error
