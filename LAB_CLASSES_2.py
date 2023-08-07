class BankAccount :
    def __init__(self, account_holder , initial_balance=0 ) -> None:
        self.account_holder=account_holder
        self.balance=initial_balance

    def desposit(self, amount):
        self.balance+=amount 
        return self.balance 
      
    def withdraw(self, amount ):
        if amount > self.balance:
          print("insufficient funds")
          return self.balance
        
        else:
           self.balance-=amount
           return self.balance

    
    
    def get_balance(self):
       return self.balance
    
    def get_account_holder(self):
       return self.account_holder
            
    
      
account1=BankAccount("Ahmad", 100000)
print(account1.get_account_holder())
print(account1.get_balance())
account1.desposit(300)
print (account1.get_balance())
account1.withdraw(300000) #here will display the message
print(account1.get_balance())
account1.withdraw(1500) 
print(account1.get_balance())
