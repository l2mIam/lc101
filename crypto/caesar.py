"""
LaunchCode lc101 Crypto assignment due 5/14/2017 11:59pm
Caesar
"""
__author__ = "Loren Milliman"
__date__ = "5/8/2017"

import unittest
from helper import rotate_character

def encrypt(word, rot):
    """ takes a string and shifts each char by rot
    PARAM1: word (str): A string
    PARAM2: rot (int): How far to rotate
    RETURN: (str): The string rotated
    """
    rot_word = ""
    for char in word:
        rot_word += str(rotate_character(char, rot))
    return rot_word

class TestCaesarMethods(unittest.TestCase):
    """ tests for Caesar methods """
    def test_encrypt(self):
        """ test encrypt """
        self.assertEqual(encrypt("foo#bar", 3), "irr#edu")
        self.assertEqual(encrypt("aZ@#$mYbA", 0), "aZ@#$mYbA")
        self.assertNotEqual(encrypt("a", 5), "b!")
        self.assertEqual(encrypt("fY", -15), "qJ")

def main():
    """ Get user input and display encrypted message """
    uncrypted = input("Type a message: ")
    rot = input("rotation factor: ")
    print str(encrypt(uncrypted, rot))
    return None

if __name__ == '__main__':
    main()
    # unittest.main()
