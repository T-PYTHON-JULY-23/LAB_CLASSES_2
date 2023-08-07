class BankAccount():
    def __init__(self,account_holder:str, initial_balance:float=0) -> None:
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance
      

    def deposit(self, amount:float):
        self.__initial_balance+= amount
        print("the amount deposit is: ")
        return self.__initial_balance

    def withdraw(self, amount:float):
        if self.__initial_balance >= amount:
            self.__initial_balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def get_balance(self):
        return self.__initial_balance
    
    def get_account_holder(self):
        return self.__account_holder            
    



    



        


account1 = BankAccount("Lenah",200)


print(account1.deposit(100))
print(account1.withdraw(50))
print(account1.get_balance())

print(f"Account Holder{account1.get_account_holder}, Balance{account1.get_balance}")







    
