"""l2m initials implimentation"""
def get_initials(the_fullname):
    """ Given a person's name, returns the person's initials (upper case) """
    my_initials = ''
    for name in the_fullname.split():
        my_initials += name[0].upper()
    return my_initials

def main():
    """ by wrapping in a main function this code will
    not run when imported and called """
    foobar = "there once was a dudette from Nantucket"
    print(foobar)
    get_initials(foobar)
    # test if get_initials affects foobar
    print(foobar)
    print(get_initials("monkey man in the middle") == "MMITM")

if __name__ == '__main__':
    main()
