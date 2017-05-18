"""
LaunchCode lc101 Crypto assignment due 5/14/2017 11:59pm
Vigenere
"""
__author__ = "Loren Milliman"
__date__ = "5/8/2017"

import unittest
from helper import rotate_character, alphabet_position, is_alpha

def encrypt(word, key):
    """ takes a string and shifts each char by rot
    PARAM1: word (str): A string
    PARAM2: key (str): rotation key
    RETURN: (str): The string rotated
    """
    key_size = len(key)
    if key_size == 0:
        return word
    key_item = 0
    rot_word = ""
    for char in word:
        if is_alpha(char):
            rot_word += str(rotate_character(char, alphabet_position(key[key_item % key_size])))
            key_item += 1
        else:
            rot_word += char
    return rot_word

class TestVigenereMethods(unittest.TestCase):
    """ tests for Caesar methods """
    def test_encrypt(self):
        """ test encrypt """
        self.assertEqual(encrypt("foo#bar", "Bbc"), "gpq#cbt")
        self.assertEqual(encrypt("!@#$%^&", "MainMonkeyBusiness"), "!@#$%^&")
        self.assertEqual(encrypt("abcdefg", " "), "fghijkl")
        self.assertEqual(encrypt("alpha", "123"), "qchxr")
        self.assertEqual(encrypt("another", ""), "another")

def main():
    """ get user input and display encrypted message
    """
    message = input("Type a message: ")
    key = str(input("Encryption key: "))
    print(encrypt(message, key))
    return None

if __name__ == '__main__':
    main()
    # unittest.main()
