"""
Python Starter
Example starter code and some notes on Python conventions...
More on Python Conventions: https://www.python.org/dev/peps/pep-0008/
Here specifiy the who, what, when and why.  There are a lot of
module level "dunders" you can use, e.g. __version__.  These are good for
acedemic purposes, but most often will be tracked by a respository in a
production environment.  The original author and creation date will not change
and are good to have for reference. Put the what and why in these comments.
Licensing, distribution, and other notes go in separate files.
"""
__author__ = "author name"
__date__ = "the date"

# any imports go here
# e.g. from SomeClass import specific_funtion
import unittest
from sys import argv

class SomeClass:
    """ Description of Some Class goes here """

    def __init__(self, the_val):
        # set up initial values.
        # Executes when a new object of this type is instantiated (created)
        self.my_val = the_val
        # double underline makes the property private
        self.__my_size = 0

    def get_my_size(self):
        """ getter for __my_size, returns the private property """
        # Private properties can only be accessed through accessors (get/set)
        # This is called encapsulation.  This is done to control how properties
        # are allowed to be modified.
        return self.__my_size

    def set_my_size(self, new_size):
        """ setter for __my_size. validate greater than zero """
        if new_size > 0:
            self.__my_size = new_size

    def some_method(self, the_param):
        """ this function does something
        PARAM1: the_param (type) requirements for the input
        RETURN: my_val (type) what the function will return
        """
        # Use distinct variable names that will not clash with reserved words.
        # There is no performance cost in making longer variable names.
        # Longer names make the code more readable.
        my_val = the_param
        return my_val

    def __str__(self):
        """ string representation of class """

    # end of class

class SubClass(SomeClass):
    """ inherets from SomeClass """
    def __init__(self, a_val, unique_property):
        # initialize as parent
        SomeClass.__init__(self, a_val)
        # define unique values of sub class
        self.unique_property = unique_property

    def unique_method(self, a_param):
        """ a method unique to SubClass """
        if self.unique_property:
            # make a call to method in parent class
            return SomeClass.some_method(self, a_param)
        return a_param*2 + 3

class TestSomeClass(unittest.TestCase):
    """ tests for SomeClass methods. Typically you will put your tests in
    a separate file, e.g. test_starter.py.  For more info, see:
    https://docs.python.org/3/library/unittest.html
    """
    def setUp(self):
        self.some_class = SomeClass("foo")

    def test_some_class_setup(self):
        """ test setup """
        self.assertEqual(self.some_class.my_val, "foo", 'correct value set')
        self.assertEqual(self.some_class.get_my_size(), 0, 'correct size set')

    def test_some_method(self):
        """ test some_method """
        self.assertTrue(self.some_class.some_method("bar") == "bar")
        self.assertFalse(self.some_class.some_method("foo") == "bar")

def main(argv):
    """ the code here executes if this file is launched directly.
    This code will NOT execute if the methods are called from another file.
    Put main last so called methods from this file will already be declared.
    """
    my_obj = SubClass(argv[1], argv[2])
    print "check it out: " + str(my_obj.unique_method(24))
    exit()

if __name__ == '__main__':
    main(argv)
    # used for running unit tests, see TestSomeClass above
    # unittest.main()
