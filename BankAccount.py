
class BankAccount:

    def __init__(self,account_holder:str,initial_balance = 0) -> None:
       
        self.account_holder = account_holder
        self.initial_balance = initial_balance


    def Deposit(self,amount):
       
       self.initial_balance = amount + self.initial_balance
       return self.initial_balance
    
    def Withdraw(self,amount):

        if amount <self.initial_balance:
            self.initial_balance  = self.initial_balance - amount
            return self.initial_balance 
        else:
            print("Error: there aren't sufficient funds in the account!! ")

    def Get_balance(self):
        return self.initial_balance

    def Get_account_holder(self):
        return self.account_holder
    
acount = BankAccount("Ahmad",500)

print(f"\nAcount befor deposet: {acount.Get_balance()}\n")
acount.Deposit(500)
print("Deposet 500 to acount.\n")

print(f"Acount after deposet: {acount.Get_balance()}\n")

print("_"*30)
print(f"\nAcount befor withdraw: {acount.Get_balance()}\n")
acount.Withdraw(500)
print("Withdraw 500 from acount.\n")

print(f"Acount after Withdraw: {acount.Get_balance()}\n")