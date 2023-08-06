class BankAccount():
    def __init__(self, account_holder:str,initial_balance:0) -> None:
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance
    def deposit(self,amount:int):
        self.__initial_balance = self.__initial_balance + amount
        print(self.__initial_balance)
    def withdraw(self,amount:int):
        if self.__initial_balance >= amount:
            self.__initial_balance = self.__initial_balance-amount
            print(self.__initial_balance)
        else:
            print(f"You don't have enough money {self.__initial_balance} !")
    def get_balance(self):
        print(self.__initial_balance)
    def get_account_holder(self):
        print(self.__account_holder)


account1 = BankAccount("Naif",150)

account1.get_account_holder()

account1.get_balance()
account1.withdraw(40)