#Create a Python class called `BankAccount` that simulates a simple bank account.
class BankAccount:
    def __init__(self,account_holder:str , initial_balance=0) -> None:
        self.__account_holder = account_holder
        self.__initial_blance = initial_balance
    def deposit(self,amount) :
            self.__initial_balance =+ amount
            return self.__initial_balance
    def withdraw (self,amount):
         if self.__initial_balance >= amount: 
              return f'not enough money'
         else:
              self.__initial_blance = self.__initial_balance - amount
              return self.__initial_balance
    def get_balance(self):
         return self.__initial_blance
    def get_account_holder (self) -> str :
         return self.__account_holder
account_ = BankAccount("Futon Alqahtani",200)
print(account_.get_account_holder())
print("Your account balance : ",account_.get_balance())
account_.deposit(150)
print("Your account after deposite: ",account_.get_balance())
print("Your account After withdraw: ",account_.withdraw(50))
print("The Final Account balance is ",account_.get_balance())