class BankAccount:
    def __init__(self, account_balance: float):
        self.current_balance = account_balance
        

    def deposit(self, amount):
        self.current_balance += amount
        return self.current_balance

    def withdraw(self, amount):
       if self.current_balance - amount < 0:
           return False
       else:
           return True

    def display_balance(self):
        print(f"Current Balance: ${self.current_balance:.2f}")