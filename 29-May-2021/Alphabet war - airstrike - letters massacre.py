"""
Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters called airstrike to help them in war - dashes and dots are spreaded everywhere on the battlefield.

Task
Write a function that accepts fight string consists of only small letters and * which means a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3 
 b - 2
 s - 1
The right side letters and their power:

 m - 4
 q - 3 
 d - 2
 z - 1
The other letters don't have power and are only victims.
The * bombs kills the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );

Example
AlphabetWar("s*zz");           //=> Right side wins!
AlphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
AlphabetWar("zzzz*s*");       //=> Right side wins!
AlphabetWar("www*www****z");  //=> Left side wins!
"""
def alphabet_war(fight):
    result = "Let's fight again!"
    left_side = ['s', 'b','p','w']
    right_side = ['z','d','q','m']
    left_point, right_point = 0,0
    centered_fight = fight.center(len(fight)+2)
    for i in range(len(fight)):
        if fight[i] in left_side and centered_fight[i] != "*" and centered_fight[i+2] != "*":
            left_point += left_side.index(fight[i]) + 1
        elif fight[i] in right_side and centered_fight[i] != "*" and centered_fight[i+2] != "*":
            right_point += right_side.index(fight[i]) + 1
    if left_point>right_point:
        result = "Left side wins!"
    elif right_point>left_point:
        result = "Right side wins!"
    return result

print((alphabet_war("zzpd**b*spsqqmbb")))
