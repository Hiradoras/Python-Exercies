"""
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""


def multiplication_table(size):
    k = []
    for i in range(1, size + 1):
        row = []
        for a in range(i, i*size+1,i):
            row.append(a)
        k.append(row)
    return k


print(multiplication_table(2))  
