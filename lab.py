class BankAccount:

    def __init__(self, account_holder, initial_balance=0) -> None:
            self.__account_holder = account_holder
            self.__initial_balance =  initial_balance
            
            print(" Welcome to the Bank Account" )

    def deposit(self, amount):
        self.__initial_balance += amount
        print("\n Amount Deposited:",amount)
        return self.__initial_balance

    def withdraw(self,amount):
        if self.__initial_balance >= amount:
            self.__initial_balance = self.__initial_balance- amount
            print("\nYou Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def get_balance(self):
        return self.__initial_balance
    def get_account_holder(self):
          return self.__account_holder
         


account=BankAccount("Sarah Alhamad", 1000)
print(account.get_account_holder())
print("account balance : ",account.get_balance())
account.deposit(300)
print("Your account after deposite: ",account.get_balance())
print("account After withdraw: ",account.withdraw(100))
print("Final Account balance is ",account.get_balance())