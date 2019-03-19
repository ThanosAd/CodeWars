# Code for 'Transform To Prime' Kata - 6 Kyu
# https://www.codewars.com/kata/5a946d9fba1bb5135100007c

def minimum_number(numbers):
    sum = 0
    for x in numbers:
        sum = sum + x
    t = sum
    flag = False
    while flag == False:
        flag1 = True
        for y in range(2,t):
            k = t/y
            if k.is_integer():
                flag1 = False
                break
        if flag1 == True:
            flag = True
        else:
            t = t + 1
    q = t - sum
    return q
