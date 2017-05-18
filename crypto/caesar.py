"""
LaunchCode lc101 Crypto assignment due 5/14/2017 11:59pm
Caesar
"""
__author__ = "Loren Milliman"
__date__ = "5/8/2017"


def alphabet_position(letter):
    """ takes a letter and returns the numeric value (a/A = 0 to z/Z = 25)
    PARAM1: letter (string): A single char (a-Z)
    RETURN: number (int): {0-25}
    """
    return (ord(letter) - 1) % 32

def rotate_character(char, rot):
    """ takes a character and rotation and returns a characters that is the
    result of rotating char by rot
    PARAM1: char (str): A single char (a-Z)
    PARMA2: rot (int): How far to rotate
    RETURN: rot_char (str): The result of rotating from char
    """

    # Use alphabet_position, add rot, mod by 26
    # get char from num
    # maybe create a new helper method, position_to_char(number)?

    return rot_char

def main():
    # Tests for alphabet_position
    assert alphabet_position('a') == 0
    assert alphabet_position('A') == 0
    assert alphabet_position('z') == 25
    assert alphabet_position('Z') == 25
    assert alphabet_position('d') == 3
    assert alphabet_position('G') == 6

    # Tests for rotate character
    
    return None

if __name__ == '__main__':
    main()
