class BalanceProvider:
    def get_balance(self):
        # Logic to fetch balance from a database or external service
        return 1500

class Account:
    def __init__(self, balance_provider):
        self.balance_provider = balance_provider
        self.balance = self.balance_provider.get_balance()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

# Creating a balance provider
balance_provider = BalanceProvider()

# Creating an account with balance injected from the balance provider
account = Account(balance_provider=balance_provider)

# Making transactions
account.deposit(500)
account.withdraw(200)

print("Remaining balance:", account.balance)
