class BankAccount:
    def __init__(self,account_holder,initial_balance=0):
       self.account_holder=account_holder
       self.balance=initial_balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds.")
            return self.balance
        
    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder
   

    
    
