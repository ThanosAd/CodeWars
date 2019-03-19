# Code for 'Build Tower' Kata - 6 kyu
# https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    list1 = list()
    z = 2*n_floors - 1
    k = 0 
    v = 0
    str = ''
    for x in range (n_floors-1,-1,-1):
        for y in range(0,k):
            str = str + ' '
        for y in range(0,z):
            str = str + '*'
        for y in range(0,v):
            str = str + ' '
        k = k + 1
        v = v + 1
        z  = z - 2
        list1.append(str)
        str =''
    return list(reversed(list1))
