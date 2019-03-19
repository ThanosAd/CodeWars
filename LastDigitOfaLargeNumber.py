# Code For 'Last digit of a large number' Kata - 5 Kyu
# https://www.codewars.com/kata/5511b2f550906349a70004e1

def last_digit(a, b):
    
    result=1
    numberOfLoops=0
	
    if b==0:
        return 1
    elif b==1:
        return a
    elif b%4==1:
        return int(str(a)[-1])
    elif b%4>1:
        numberOfLoops = b%4
    else:
        numberOfLoops = b%4+4
        print(numberOfLoops)
    
    for x in range(0,numberOfLoops):
        result = result*int(str(a)[-1])
        print(result)
    
    return int(str(result)[-1])
