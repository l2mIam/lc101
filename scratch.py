# TODO
# define a function called sum_evens, which receives one argument, a list of numbers.
# your function should return the sum of all the even numbers in the list
def sum_evens(the_list):
    total_even=0
    for i in range(len(the_list)):
        if type(the_list[i]) == type(1) and the_list[i]%2==0:
            total_even=total_even+the_list[i]
    return total_even
