"""
Binary Search
"""
__author__ = "l2m"
__date__ = "6/6/17"

import unittest

class BS:
    """ A search function """

    def __init__(self):
        """ start some BS """

    @staticmethod
    def binary_search(arr, item):
        """ search for item in arr: return index if found else return -1
        PARAM1: arr (list): the array to search
        PARAM2: item (val): some comparable value
        RETURN: (int) index of item, or -1 if item not found.
        """
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = low + high
            guess = arr[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return -1

class Tests(unittest.TestCase):
    """ tests for binary search """
    def setUp(self):
        self.arr_nums = [1, 2, 3, 4, 6, 9, 10, 12, 15, 18, 20, 25, 40, 60, 75, 89, 99]
        self.arr_chars = ['a', 'c', 'd', 'f', 'g', 'y', 'z']

    def test_binary_search(self):
        """ test binary search """
        self.assertEqual(BS.binary_search(self.arr_nums, 4), 3)
        self.assertEqual(BS.binary_search(self.arr_nums, 1), 0)
        self.assertEqual(BS.binary_search(self.arr_nums, 19), -1)
        self.assertNotEqual(BS.binary_search(self.arr_nums, 99), -1)
        self.assertNotEqual(BS.binary_search(self.arr_chars, 'g'), 5)
        self.assertEqual(BS.binary_search(self.arr_chars, 'f'), 3)
        self.assertEqual(BS.binary_search(self.arr_chars, 'z'), 6)
        self.assertEqual(BS.binary_search(self.arr_chars, 'm'), -1)

if __name__ == '__main__':
    unittest.main()
    