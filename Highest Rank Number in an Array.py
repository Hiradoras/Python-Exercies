"""
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
"""


def highest_rank(arr):
    mod = 0
    for i in arr:
        if arr.count(i) >= arr.count(mod):
            if arr.count(i) == arr.count(mod):
                mod = i if i >= mod else mod
            else:
                mod = i
    return mod


print(highest_rank([2,2,1,1,4,4,3,3]))