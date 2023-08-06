"""# LAB_CLASSES_2

Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should print an error message and leave the balance unchanged.
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.

"""

class Bank():

    def __init__(self,account_name:str,init_blance:float =0) -> None:

        self.__account_name=account_name
        self.__init_balnce=init_blance

    def deposit(self ,amount:float):
            self.__init_balnce+=amount
            return self.__init_balnce

    def withdraw(self , amount:float) -> float:
        
        if self.__init_balnce  >= amount : 
            self.__init_balnce-=amount
        else : 
            print("Blance is not enough ")



    def get_blance(self) -> float:
        return self.__init_balnce
    
    def get_account_name(self) -> str :
        return self.__account_name




my_account=Bank("Khaled alghamdi",100)

print(f'blance before desposit 100$   :{my_account.get_blance()} ')

my_account.deposit(100)

print(f'blance after desposit 100$    :{my_account.get_blance()} ')

my_account.withdraw(200)

print(f'blance after withdraw 200$    :{my_account.get_blance()} ')


