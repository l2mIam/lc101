""" LC101 chapter assignment """

# Chapter 9 assignment
def reverse_string(the_string):
    """ return the reverse the given string """
    # iterating by index in reverse
    # my_rev = ""
    # for idx in range(len(the_string) - 1, -1, -1):
    #     my_rev += the_string[idx]
    # return my_rev

    # using a while loop
    my_rev = ""
    idx = len(the_string) - 1
    while idx >= 0:
        my_rev += the_string[idx]
        idx -= 1
    return my_rev


def mirror_string(the_string):
    """ return the mirror of the given string """
    return the_string + reverse_string(the_string)


# Chapter 10 assignment
def sum_evens(the_list):
    """ define a function called sum_evens, which receives one argument, a list of numbers.
        your function should return the sum of all the even numbers in the list """
    my_sum = 0
    for num in the_list:
        if num % 2 == 0:
            my_sum += num
    return my_sum


# Chapter 11 assignment

def main():
    """ tests for chapter assignments"""
    print("Chap 9 (reverse_string): " + str(reverse_string("foobar") == "raboof"))
    print("Chap 9 (mirror_string): " + str(mirror_string("foobar") == "foobarraboof"))
    print("Chap 10 (sum_evens): " + str(sum_evens([2, 3, 4]) == 6))
    print("Chap 10 (sum_evens): " + str(sum_evens([]) == 0))
    print("Chap 10 (sum_evens): " + str(sum_evens([0, 7, 2, 4, 2, 1]) == 8))
    print("Chap 10 (sum_evens): " + str(sum_evens([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20))
    print("Chap 10 (sum_evens): " + str(sum_evens(range(200, 500)) == 52350))
    
if __name__ == "__main__":
    main()
