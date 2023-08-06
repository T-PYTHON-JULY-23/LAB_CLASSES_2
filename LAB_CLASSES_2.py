


class BankAccount:

    def __init__(self,account_holder:str,initial_balance=0) -> None:
        self.account_holder=account_holder
        self.initial_balance=initial_balance



    def deposit(self,amount:int):
        UpdatedBalance = self.initial_balance+amount
        self.initial_balance=UpdatedBalance
        return UpdatedBalance



    def withdraw (self,amount:int):
        if self.initial_balance > amount:
           UpdatedBalance=(self.initial_balance - amount)
           self.initial_balance=UpdatedBalance
           return UpdatedBalance
        
        elif self.initial_balance < amount:
            raise UnboundLocalError("sorry balance is not allowed")

  
    def get_balance(self):
        return self.initial_balance
    
    def get_account_holder (self):
        return self.account_holder
    


user1=BankAccount("nada",5000)
user2=BankAccount("sara",10000)
user3=BankAccount("lama")
try:
  print(user1.get_balance())
  print(user1.deposit(2000))
  print(user1.withdraw(2000))
  print(user1.withdraw(7000))
  print(user1.get_account_holder())

except UnboundLocalError:
  print("sorry balance is not allowed")







        



