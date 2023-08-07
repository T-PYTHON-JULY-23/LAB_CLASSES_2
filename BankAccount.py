class BankAccount:
    def __init__(self, account_holder, initial_balance=0 ) -> None:
        self.account_holder=account_holder
        self.initial_balance=initial_balance

    def deposit(self,amount):
        self.initial_balance +=amount
        return f"Balance ubdated with: {amount}, now its: {self.initial_balance}"
    
    def withdraw (self,amount):
        if self.initial_balance>= amount:
            self.initial_balance-=amount
            return f"Balance ubdated to {self.initial_balance}"
        else: 
            return(f"Sory {self.account_holder} your balance is not enough to complete this process.. ")
            
    def get_balance(self):
        return f"Current balance is: {self.initial_balance}"
    def get_account_holder(self):
        return f"Name of account holder: {self.account_holder}"
    
Maram_account=BankAccount('Maram Fahad',1500)

print(Maram_account.get_account_holder())
print(Maram_account.get_balance())
print(Maram_account.deposit(3000))
print(Maram_account.withdraw(2000))
print(Maram_account.withdraw(3000))