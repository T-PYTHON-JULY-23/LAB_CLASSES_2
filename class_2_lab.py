

class BankAccount :
    
    def __init__(self, account_holder:str, initial_balance:float):
        self.account_holder = account_holder
        self.initial_balance = initial_balance 

    def deposit (self ,amount):
        self.initial_balance += amount
        return f" the initial balance is {self.initial_balance}"

    def withdraw (self ,amount):
         if amount >= self.initial_balance:
            print("funds not enough. Withdrawal canceled.")
            
         else:
           self.initial_balance -= amount
         return self.initial_balance

    def get_balance (self):
        return self.initial_balance
    
    def get_account_holder (self, account_holder):
        return f" the name of owner is {account_holder} "
    
    
    
person1 = BankAccount("hassan", 500)

print("Account holder:", person1.get_account_holder(" \nHassan"))
print("Current balance:", person1.get_balance())

person1.deposit(0)
print("Balance after deposit:", person1.get_balance())
print("Balance after withdrawal:", person1.withdraw(100))
print("the Existing Balance :", person1.get_balance())

 

        