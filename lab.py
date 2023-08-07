class BankAccount :
    def __init__(self,account_holder,initial_balance=0) -> None:
        self.__account_holder=account_holder
        self.__initial_balance=initial_balance
      
    def deposit(self,amount):
       
        new_balance= self.__initial_balance=+amount

        return new_balance
    def withdraw(self,amount):
        if self.__initial_balance<amount:
           return f"there aren't sufficient funds in the account"
        else:
            new_balance= self.__initial_balance=-amount
            return new_balance
    def get_balance(self):
        return f" current account balance is: {self.__initial_balance}"
    
    def get_account_holder(self):
        return f"name of the account holder is: {self.__account_holder} "
  
account1=BankAccount("hamad",5000)
account2=BankAccount("lama",80000)
account3=BankAccount("ghaida",100000)
print(account1.get_balance())
print(account1.get_account_holder())
print(account1.deposit(1000))
print(account1.get_balance())