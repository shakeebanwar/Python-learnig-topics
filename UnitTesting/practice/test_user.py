import unittest
from user import User



class TestUserClass(unittest.TestCase):
    def setUp(self):
        """ Create a instance of User class"""
        self.user1 = User("John", "Doe")
        self.user2 = User("Jane", "Smith")

    def tearDown(self):
        """ Common cleanup method called after each test case """
        del self.user1
        del self.user2

    def test_full_name(self):
        """ Test the full_name property """
        self.assertEqual(self.user1.full_name, "John Doe")
        self.assertEqual(self.user2.full_name, "Jane Smith")

    def test_change_first_name(self):
        """ Test changing first_name property """
        self.user1.first_name = "Mike"
        self.assertEqual(self.user1.full_name, "Mike Doe")

    def test_change_last_name(self):
        """ Test changing last_name property """
        self.user2.last_name = "Johnson"
        self.assertEqual(self.user2.full_name, "Jane Johnson")

if __name__ == '__main__':
    unittest.main()