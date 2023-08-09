#with out inversion

print("without inversion")
class TransactionHandler:
    def __init__(self):
        self.transaction_service = TransactionService()

    def process_transaction(self, amount):
        self.transaction_service.perform_transaction(amount)

class TransactionService:
    def perform_transaction(self, amount):
        print(f"Performing transaction of amount {amount}")


history = TransactionHandler()
print(history.process_transaction(1000))


"""
Is example mein TransactionHandler class TransactionService class ko directly create kar raha hai, yani yeh Dependency Inversion Principle ko follow nahi kar raha hai.


Limitation without Dependency Inversion Principle:

    Tightly Coupled Code: TransactionHandler class directly depends on TransactionService, making it tightly coupled. Agar future mein aapko transaction processing ka process change karna ho, toh aapko TransactionHandler class mein changes karne honge.

    Inflexibility: Agar aapko TransactionHandler ko different services ke sath use karna ho (for example, testing ke liye mock service), toh aapko TransactionHandler class ke code mein changes karna hoga.

    Difficult Testing: Unit testing TransactionHandler class becomes difficult because it's directly coupled with TransactionService.
"""

#with inversion

print("with inversion")

class TransactionServiceProvider:
    def perform_transaction(self, amount):
        pass

class TransactionService(TransactionServiceProvider):
    def perform_transaction(self, amount):
        print(f"Performing transaction of amount {amount}")

class TransactionHandler:
    def __init__(self, transaction_service_provider):
        self.transaction_service_provider = transaction_service_provider

    def process_transaction(self, amount):
        self.transaction_service_provider.perform_transaction(amount)

# Using Dependency Inversion to inject the transaction service provider
service = TransactionService()
handler = TransactionHandler(transaction_service_provider=service)

# Process a transaction
handler.process_transaction(100)
