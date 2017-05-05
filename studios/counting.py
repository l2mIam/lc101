"""
LaunchCode lc101 Studio for 5/3/2017
Counting
"""
__author__ = "Loren Milliman"
__date__ = "5/3/2017"

def counting(the_string):
    """ Returns the character count for each character found in the input
    PARAMS: the_string (string)
    RETURN: my_counts (dictionary)
    """
    my_counts = {}
    for char in the_string:
        if my_counts.has_key(char):
            my_counts[char] += 1
        else:
            my_counts[char] = 1
    # print my_counts
    return my_counts

def main():
    """ Counting Studio tests"""
    # typically a method like counting would just return the dictionary
    # without printing anything. Then you would print here if you wanted.
    print counting("hey I just printed the return value!")

    # force a given output order for only characters I want
    counts = counting("it's all foobar")
    chars = "aeiou"
    output = "Character counts\n"
    for char in chars:
        if counts.has_key(char):
            output += char + ": " + str(counts[char]) + "\n"
    print output

    # tests to spot check results
    counts = counting("5aaaaabbb")
    print str(counts.get("a")) == "5"
    print str(counts.get("5")) == "1"
    print str(counts.get("c")) == "None"

if __name__ == '__main__':
    main()
