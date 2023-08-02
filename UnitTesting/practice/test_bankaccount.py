import unittest
from bankaccount import BankAccount

class TestBankAccountClass(unittest.TestCase):
 
    def setUp(self):
        """ Create a instance of BankAccount class"""
        self.account = BankAccount()

 
    def tearDown(self):
        # Common cleanup method called once after all test cases
        del self.account

    def test_initial_balance(self):
        """ Test if initial balance is 0 """
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        """ Test depositing money and check if balance updates correctly """
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw_sufficient_balance(self):
        """ Test withdrawing money with sufficient balance """
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_insufficient_balance(self):
        """ Test withdrawing money with insufficient balance """
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

if __name__ == '__main__':
    unittest.main()