class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

# Creating an account
account = Account(balance=1000)

# Making transactions
account.deposit(500)
account.withdraw(200)

print("Remaining balance:", account.balance)
