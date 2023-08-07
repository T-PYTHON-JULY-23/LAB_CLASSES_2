class BankAccount:

    def __init__(self, account_holder:str , initial_balance:float)->None:
        self.__account_holder = account_holder 
        self.__initial_balance = initial_balance

    def deposit(self, amount:float):
       balance:float = self.__initial_balance + amount
       self.__initial_balance= balance
       return balance
       
    def withdraw(self, amount:float):
         
         if self.__initial_balance > amount:
          balance:float = self.__initial_balance - amount
          self.__initial_balance= balance
          return balance

         else:
            return( "There is insufficient balance!")
             

    def get_balance(self):
        return self.__initial_balance 

    def get_account_holder(self):
         return self.__account_holder


account1= BankAccount("Sarah",28375)

print(account1.withdraw(700))
print(account1.deposit(500))
print(account1.get_balance())



account2= BankAccount("Afnan",0)
print(account2.deposit(500))
print(account2.withdraw(700))
print(account2.get_balance())


print(f"Account holder: {account1.get_account_holder()}, Balance: {account1.get_balance()}")
print(f"Account holder: {account2.get_account_holder()}, Balance: {account2.get_balance()}")
