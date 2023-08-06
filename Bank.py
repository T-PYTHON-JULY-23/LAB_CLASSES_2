# LAB_CLASSES_2
# Create a Python class called BankAccount that simulates a simple bank account. The class should have the following functionalities:
class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float = 0) -> None:
        self.account_holder = account_holder
        self.initial_balance = initial_balance
    def deposit(self,amount:float):
        self.initial_balance = self.initial_balance + amount
        return f"your balance is {self.initial_balance}$"
    def withdraw(self,amount):
        if self.initial_balance >= amount:
            self.initial_balance = self.initial_balance - amount 
            return f"{self.initial_balance}$"
        else:
            f"Your account have insufficient funds {self.initial_balance}$"

    def get_balance(self):
        return f"{self.initial_balance}$"
    def get_account_holder(self):
        return f"Your name is : {self.account_holder}"
MyAccount = BankAccount("Abdulmalik",200)


print(MyAccount.get_account_holder())
print("Your account balance : ",MyAccount.get_balance())
MyAccount.deposit(150)
print("Your account after deposite: ",MyAccount.get_balance())
print("Your account After withdraw: ",MyAccount.withdraw(50))
print("Final Account balance is ",MyAccount.get_balance())


# It should have a constructor that accepts the account_holder name and initial balance (initial_balance), setting the balance to zero if the initial balance is not provided.
# A method called deposit that accepts an amount and adds it to the account balance, and then returns the updated balance.
# A method called withdraw that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
# A method called get_balance that returns the current account balance.
# A method called get_account_holder that returns the name of the account holder.