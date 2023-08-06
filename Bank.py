class BankAccount: #Create a Python class 
    def __init__(self,account_holder , initial_balance=0):
        self.account_holder=account_holder
        self.initial_balance=initial_balance

    def deposit(self ,amount): #this fun accepts an amount and adds it to the account balance, and then returns the updated balance.
        self.amount=amount
        print(f"The amount : ({amount}) has been added successfully")
        return self.initial_balance + amount
    
    def withdraw (self , amount):  # this fun accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account.
        if amount < self.initial_balance:
            self.initial_balance -= amount
            return self.initial_balance
        else:
            print("Insufficient funds. Withdrawal cannot be processed")


    def get_account_holder(self):    #returns the name of the account holder.
        return print (f"name of the account holder is : {self.account_holder}")
    

    def get_balance (self):  #returns the current account balance.
        return print(f"current account balance is :{self.initial_balance}")
    
    
    

account1= BankAccount("noura",6000)
account2= BankAccount("saud " , 120000)
account3=BankAccount("firas",500)

print(account1.get_account_holder())  
print(account1.get_balance()) 

print(account2.get_account_holder())  
print(account2.get_balance()) 

print(account3.get_account_holder())  
print(account3.get_balance()) 


print(account2.withdraw(200))
account3.withdraw(600)  #This will display an error message since there are insufficient funds.
account1.deposit(20000)