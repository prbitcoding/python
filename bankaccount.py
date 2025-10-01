class InsufficientFundsError(Exception):
    pass

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot withdraw {amount}: insufficient funds.")
        self.balance -= amount
        print(f"Withdrew: {amount}, New balance: {self.balance}")

    def __enter__(self):
        print("Entering account context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception occurred: {exc_value}")
        print("Exiting account context.")
        return False

 
try:
    with Account(1000) as account:
        account.deposit(500)
        account.withdraw(1200)
        account.withdraw(500)   
except InsufficientFundsError as e:
    print(f"Error: {e}")
