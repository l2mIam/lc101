"""
LaunchCode lc101 Crypto assignment due 5/14/2017 11:59pm
Caesar
"""
__author__ = "Loren Milliman"
__date__ = "5/8/2017"


def alphabet_position(letter):
    """ takes a letter and returns the numeric value (a/A = 0 to z/Z = 25)
    PARAM1: letter (string): A single char [a,z] or [A,Z]
    RETURN: number (int): [0,25]
    """
    return (ord(letter) - 1) % 32

def position_to_char(number, upper):
    """ takes a position [0,25] and returns character [a,z] or [A,Z]
    PARAM1: number (int): a single integer [0,25]
    PARAM2: upper (bool): True if upper case
    RETURN: char (string): a single character [a,z], if upper: [A,Z]
    """
    mod = 65 if upper else 97
    return chr(number + mod)

def is_upper(char):
    """ takes a single character and returns true if uppercase
    PARAM1: char (string): a single charager [a,z] or [A,Z]
    RETURN: (bool): true if char [A,Z]
    """
    return ord(char) < 97

def rotate_character(char, rot):
    """ takes a character and rotation and returns a characters that is the
    result of rotating char by rot
    PARAM1: char (str): A single char [a,z] or [A,Z]
    PARMA2: rot (int): How far to rotate
    RETURN: rot_char (str): A single character [a,z] or [A,Z] the result of rotating from char
    """
    return position_to_char((alphabet_position(char) + rot) % 26, is_upper(char))

def main():
    """ Just some tests
    """
    # Tests for alphabet_position
    assert alphabet_position('a') == 0
    assert alphabet_position('A') == 0
    assert alphabet_position('z') == 25
    assert alphabet_position('Z') == 25
    assert alphabet_position('d') == 3
    assert alphabet_position('G') == 6

    # Tests for position_to_char
    assert position_to_char(0, False) == 'a'
    assert position_to_char(25, False) == 'z'
    assert position_to_char(4, True) == 'E'

    # Tests for is_upper
    assert is_upper('A')
    assert is_upper('Z')
    assert not is_upper('a')
    assert not is_upper('z')

    # Tests for rotate_character
    assert rotate_character('A', 5) == 'F'
    assert rotate_character('z', 3) == 'c'
    assert rotate_character('Y', 28) == 'A'

    return None

if __name__ == '__main__':
    main()
