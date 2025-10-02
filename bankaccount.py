class InsufficientError(Exception):
    pass

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientError(f"Cannot withdraw {amount}: insufficient funds.")
        self.balance -= amount
        print(f"Withdrew: {amount}, New balance: {self.balance}")

    def __enter__(self):
        print("Entering account context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Exception occurred: {exc_value}" if exc_type else "", "Exiting account context")
        return False

 
try:
    with Account(1000) as account:
        account.deposit(500)
        account.withdraw(1200)
        account.withdraw(500)   
except InsufficientError as e:
    print(f"Error: {e}")
