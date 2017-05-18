"""
LaunchCode lc101 Crypto assignment due 5/14/2017 11:59pm
Caesar
"""
__author__ = "Loren Milliman"
__date__ = "5/8/2017"

import unittest

def alphabet_position(letter):
    """ takes a letter and returns the numeric value (a/A = 0 to z/Z = 25)
    PARAM1: letter (string): A single char [a,z] or [A,Z]
    RETURN: (int): [0,25]
    """
    return (ord(letter) - 1) % 32

def position_to_char(number, upper):
    """ takes a position [0,25] and returns character [a,z] or [A,Z]
    PARAM1: number (int): a single integer [0,25]
    PARAM2: upper (bool): True if upper case
    RETURN: (string): a single character [a,z], if upper: [A,Z]
    """
    mod = 65 if upper else 97
    return chr(number + mod)

def is_upper(char):
    """ takes a single character and returns true if uppercase
    PARAM1: char (string): a single charager [a,z] or [A,Z]
    RETURN: (bool): true if char [A,Z]
    """
    return ord(char) < 97

def is_alpha(char):
    """ takes a single character and returns true if char is [a,z] or [A,Z]
    PARAM1: char (string): a single character
    RETURN: (bool):  True of char [a,z] or [A,Z]
    """
    val = ord(char)
    return (val > 64 and val < 91) or (val > 96 and val < 123)

def rotate_character(char, rot):
    """ takes a character and rotation and returns a characters that is the
    result of rotating char by rot.  Return char unmodified if char is not [a,z] or [A,Z]
    PARAM1: char (str): A single char [a,z] or [A,Z]
    PARMA2: rot (int): How far to rotate
    RETURN: (str): A single character [a,z] or [A,Z] the result of rotating from char
    """
    if not is_alpha(char):
        return char
    return position_to_char((alphabet_position(char) + rot) % 26, is_upper(char))

class TestCaesar(unittest.TestCase):
    """ tests for caesar methods """
    def test_alphabet_position(self):
        """ test alpha_position """
        self.assertEqual(alphabet_position('a'), 0)
        self.assertEqual(alphabet_position('A'), 0)
        self.assertEqual(alphabet_position('z'), 25)
        self.assertEqual(alphabet_position('Z'), 25)
        self.assertEqual(alphabet_position('d'), 3)
        self.assertEqual(alphabet_position('G'), 6)

    def test_position_to_char(self):
        """ test position_to_char """
        self.assertEqual(position_to_char(0, False), 'a')
        self.assertEqual(position_to_char(25, False), 'z')
        self.assertEqual(position_to_char(4, True), 'E')

    def test_is_upper(self):
        """ test is_upper """
        self.assertTrue(is_upper('A'))
        self.assertTrue(is_upper('Z'))
        self.assertFalse(is_upper('a'))
        self.assertFalse(is_upper('z'))

    def test_is_alpha(self):
        """ test is_alpha """
        self.assertTrue(is_alpha('a'))
        self.assertTrue(is_alpha('z'))
        self.assertTrue(is_alpha('A'))
        self.assertFalse(is_alpha('!'))
        self.assertFalse(is_alpha('~'))

    def test_rotate_character(self):
        """ test rotate_character """
        self.assertEqual(rotate_character('A', -5), 'V')
        self.assertEqual(rotate_character('z', 3), 'c')
        self.assertEqual(rotate_character('Y', 28), 'A')
        self.assertEqual(rotate_character('#', 22), '#')
        self.assertEqual(rotate_character('%', -4), '%')

def main():
    """ nothing to see here """
    return None

if __name__ == '__main__':
    unittest.main()
