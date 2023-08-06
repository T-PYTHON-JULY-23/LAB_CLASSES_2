class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float = 0) -> None:
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance
    # def set_account_holder(self, account_holder:str):
    #     if isinstance(account_holder, str):
    #         self.__account_holder = account_holder
    #     else:
    #         raise ValueError("please input valid name")
    # def set_initial_balance(self, initial_balance:float):
    #     if isinstance(initial_balance, float):
    #         self.__initial_balance = initial_balance
    #     else:
    #         raise ValueError("please input valid balance")
    def get_account_holder(self):
        return self.__account_holder
    def get_initial_balance(self):
        return self.__initial_balance
    def deposit(self,amount):
        newBlance = amount + self.__initial_balance
        self.__initial_balance = newBlance
        return f'updated balance: {self.__initial_balance}'
    def withdraw(self,amount):
        newBlance = self.__initial_balance - amount
        if newBlance >= 0:
            self.__initial_balance = newBlance
            return f'updated balance: {self.__initial_balance}'
        else:
            return 'not enough balance'


account1 = BankAccount('Renad',5000)
print(account1.get_account_holder())
print(account1.get_initial_balance())
print(account1.deposit(1000))
print(account1.withdraw(3000))
print(account1.get_initial_balance())
print(account1.withdraw(5000.1))