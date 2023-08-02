class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percentage):
        discounted_price = self.price * (1 - percentage / 100)
        return discounted_price