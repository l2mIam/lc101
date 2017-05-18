"""
LaunchCode lc101 Crypto assignment due 5/14/2017 11:59pm
Caesar
"""
__author__ = "Loren Milliman"
__date__ = "5/8/2017"

from helper import encrypt

def main():
    """ Get user input and display encrypted message """
    uncrypted = input("Type a message: ")
    rot = input("rotation factor: ")
    print(str(encrypt(uncrypted, rot)))
    return None

if __name__ == '__main__':
    main()
