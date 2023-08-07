import unittest
from sorting import sort_list

class TestSortListFunction(unittest.TestCase):
    """
    Test cases for the sort_list function.
    """

    def test_sort_empty_list(self):
        """
        Test sorting an empty list.
        """
        
        input_list = []
        sortinglist = sort_list(input_list)
        self.assertEqual(sortinglist, [])

    def test_sort_list(self):
        """
        Test sorting a list of integers.
        """

        input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sortinglist = sort_list(input_list)
        self.assertEqual(sortinglist, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
