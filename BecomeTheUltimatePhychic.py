# Code for 'Become The Ultimate Phychic' Kata - 5 Kyu
# https://www.codewars.com/kata/55b2d9bd2d3e974dfb000030

allBalls=list()
kilos=list()
sum1=list()

def a():
    global allBalls
    global kilos
    global sum1
    for r in range(0,51):
        for g in range(0,51):
            for b in range(0,51):
                if g+r+b<=50:
                    s = g*5+r*4+b*3
                    kilos.append(s)
                    sum1.append(g+r+b)
                    balls=[g,r,b]
                    allBalls.append(balls)

def Guess_it(s,k):
    
    global allBalls
    allBalls=list()
    global kilos
    kilos=list()
    global sum1
    sum1=list()
    
    a()
    listToReturn=list()
    
    for x in range(0,len(sum1)):
        if sum1[x]==s and kilos[x]==k:
            print(len(sum1))
            print(x)
            print(listToReturn)
            listToReturn.append(allBalls[x])
    listToReturn.reverse()
    return listToReturn
