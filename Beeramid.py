# Code for 'Beeramid' Kata - 5 Kyu
# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1

def beeramid(bonus, price):
    beers = bonus//price
    beersInPyramid = 0
    PotentialBeersInPyramid = 0
    level = 0
    while PotentialBeersInPyramid<beers:
        PotentialBeersInPyramid = PotentialBeersInPyramid + (level + 1)**2
        if(PotentialBeersInPyramid <= beers):
            level = level + 1
            beersInPyramid = beersInPyramid + level**2
    return level
