'''
josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!
'''
### Not Completed ###

def josephus(n,k):
    people =  [i for i in range(1, n+1)]
    looped = 1
    lower_looped = 0
    last_looped = 0
    kill_index = k-2
    while len(people) > 1:
        to_kill_index = kill_index + looped
        lower_index = to_kill_index - len(people) - lower_looped
        last_kill_index = lower_index - 1
        if len(people) <= k:
            people.pop(last_kill_index - last_looped)
            last_looped += last_kill_index + 1
            print(people)

        elif to_kill_index>len(people)-1:
            
            print(people[lower_index])
            print(f"index: {str(lower_index)}, len: {str(len(people))}")
            people.pop(lower_index)
            lower_looped += lower_index-2
        else:
            print(people[to_kill_index])
            print(f"index: {str(to_kill_index)}, len: {str(len(people))}")
            people.pop(to_kill_index)
            looped +=kill_index+1


    return people[0]


print(josephus(7,3))