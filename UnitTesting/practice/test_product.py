import unittest
from unittest.mock import patch
from product import Product


class TestProductClass(unittest.TestCase):
    def setUp(self):
        # Common setup method called before each test case
        self.product1 = Product("Laptop", 1000)
        self.product2 = Product("Phone", 500)

    def tearDown(self):
        # Common cleanup method called after each test case
        del self.product1
        del self.product2

    def test_discount_10_percent(self):
        # Test the discount method with a 10% discount
        discounted_price = self.product1.discount(10)
        self.assertEqual(discounted_price, 900)

    def test_discount_20_percent(self):
        # Test the discount method with a 20% discount
        discounted_price = self.product2.discount(20)
        self.assertEqual(discounted_price, 400)

   
if __name__ == '__main__':
    unittest.main()