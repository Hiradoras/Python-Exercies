"""
Story
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats
ex2 P O~ O~ ~O O~ has 1 deaf rat
ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
"""

def count_deaf_rats(town):
    deaf_rats = 0
    town = town.replace(" ","")
    [left,right] = town.split("P")

    for i in range(0,len(left),2):
        if left[i] == "O": deaf_rats +=1
    for i in range(0,len(right),2):
        if right[i] == "~" : deaf_rats +=1

    return deaf_rats

print(count_deaf_rats("P O~ O~ ~O O~"))