# Code for 'Validate Credit Card Number' Kata - 6 kyu
# https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2

def validate(n):
    n = [int(x) for x in str(n)]
    if len(n)%2 == 0:
        for x in range(0,len(n),2):
            n[x] = n[x]*2
    else:
         for x in range(1,len(n),2):
            n[x] = n[x]*2
    for x in range(0,len(n)):
        if n[x]>9:
            n[x] = n[x] - 9
    sum = 0
    for x in range(0,len(n)):
        sum = sum + n[x]
    if sum%10 == 0:
        return True
    return False
