'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''
def square_digits(num):
    digits = [int(i) for i in str(num)]
    result = ""
    for i in digits:
        result+=str(i**2)
    return int(result)
print(square_digits(9119))

### OR 

def square_digits_new(num):
    return int("".join(str(int(i)**2) for i in str(num)))

print(square_digits_new(9119))