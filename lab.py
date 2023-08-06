class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, blanc):
        self.initial_balance += blanc
        return self.initial_balance

    def withdraw(self, blanc):
        if blanc <= self.initial_balance:
            self.initial_balance -= blanc
        else:
            print("Insufficient funds. Withdrawal canceled.")
        return self.initial_balance

    def get_balance(self):
        return self.initial_balance

    def get_account_holder(self):
        return self.account_holder


account = BankAccount("basma Al shaharani", 5000)

print("Account holder:", account.get_account_holder())
print("Current balance:", account.get_balance())

account.deposit(0)
print("Balance after deposit:", account.get_balance())

account.withdraw(0)
print("Balance after withdrawal:", account.get_balance())

account.withdraw(0)  # This will print an error message
print("Balance after withdrawal:", account.get_balance())