class BankAccount:
    def __init__(self, account_balance):
        self.balance = account_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
       if self.balance == 0:
           return False
       else:
           return True

    def display_balance(self):
        print(f"Your current balane is {self.balance}")