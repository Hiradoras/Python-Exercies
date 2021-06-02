'''
Implement the flipfront function. Given an array of integers and a number n between 2
and the length of the array (inclusive), return the array with the order of the first n elements reversed.

flipfront([0, 1, 2, 3, 4], 2) => [1, 0, 2, 3, 4]
flipfront([0, 1, 2, 3, 4], 3) => [2, 1, 0, 3, 4]
flipfront([0, 1, 2, 3, 4], 5) => [4, 3, 2, 1, 0]
flipfront([1, 2, 2, 2], 3) => [2, 2, 1, 2]
Optionally, as an optimization, modify the array in-place (in which case you don't
need to return it). It's also fine to have the array be a global variable or member
variable, in which case you only need to pass in the argument n.
'''

def flipfront(l, n):
    sorted_part = []
    for i in range(0,n):
        sorted_part.append(l[i])
    sorted_part.reverse()
    new_l = [l[i] for i in range(n,len(l))]
    return sorted_part + new_l
print(flipfront([0, 1, 2, 3, 4], 2))
    