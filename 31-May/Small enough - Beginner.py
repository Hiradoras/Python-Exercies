'''
You will be given an array and a limit value. You must check
that all values in the array are below or equal to the limit
value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.
'''


def small_enough(array, limit):
    not_in_limit = [i for i in array if i>limit]
    print(not_in_limit)
    return True if len(not_in_limit)==0 else False


print(small_enough([66, 101] ,200))