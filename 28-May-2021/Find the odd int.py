"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""
def find_it(seq):
    odd = 0
    for i in seq:
        if seq.count(i) % 2:
            odd = i
    return odd

# Or with one line

def find_it2(seq):
    return [i for i in seq if seq.count(i) % 2][0]
    # Without the '[0]' it will return a list of wanted ints. Since we want to get an int we will takes list [0]st item.