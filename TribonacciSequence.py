# Code for 'Tribonacci Sequence' Kata - 6 Kyu
# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    if n>2:
        for x in range (2,n-1):
            nextt = 0
            for y in range(0,3):
                nextt = nextt + signature[x-y]
            signature.append(nextt)
    elif n==1:
        temp = signature[0]
        signature=[]
        signature.append(temp)
    elif n==2:
        temp1 = signature[0]
        temp2 = signature[1]
        signature = []
        signature.append(temp1)
        signature.append(temp2)
    else:
        signature = []
    
    return signature
