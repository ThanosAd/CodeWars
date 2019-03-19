# Code for'Find heavy ball - level: master' Kata - 5 Kyu
# https://www.codewars.com/kata/544034f426bc6adda200000e

def find_ball(scales):
    # call scales.get_weight() at most TWICE
    # return indexOfHeavierBall
    for i in range(1, 8):
        leftPan = [0,1,2]
        rightPan = [3,4,5]
        w = scales.get_weight(leftPan, rightPan)
        if w<0:
            leftPan = [0]
            rightPan = [1]
            w = scales.get_weight(leftPan, rightPan)
            if w < 0:
                return leftPan[0]
            if w > 0:
                return rightPan[0]
            if w == 0:
                return 2
        if w>0:
            leftPan = [3]
            rightPan = [4]
            w = scales.get_weight(leftPan, rightPan)
            if w < 0:
                return leftPan[0]
            if w > 0:
                return rightPan[0]
            if w == 0:
                return 5
        if w==0:
            leftPan = [6]
            rightPan = [7]
            w = scales.get_weight(leftPan, rightPan)
            if w < 0:
                return leftPan[0]
            if w > 0:
                return rightPan[0]
