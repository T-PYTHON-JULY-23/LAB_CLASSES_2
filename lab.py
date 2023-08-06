class BanckAccount:


    def __init__(self, account_holder:str, initial_balance:int = 0) -> None:
        self.account_holder = account_holder
        self.__balance = initial_balance


    def deposite(self, amount:int) -> str:
        new_balance = self.__balance + amount
        self.__balance = new_balance
        return f"the deposit transaction is done !\nyour updated balance is {new_balance} SAR"
    

    def withdraw(self, amount:int) -> str:
        if amount > self.__balance:
            raise ValueError("you dont have enough mony in you account")
        else:
            new_balance = self.__balance - amount
            self.__balance = new_balance
            return f"the withdraw transaction is done !\nyour updated balance is {new_balance} SAR"
    

    def get_balance(self) -> int:
        return self.__balance
    

    def get_account_holder(self) -> str:
        return self.account_holder
    

acc1 = BanckAccount("ahmad", 100)
print(acc1.account_holder)
# print(acc1.__balance)
print(f"{acc1.get_balance()} SAR")

print(acc1.deposite(6000))
print(acc1.withdraw(2300))
