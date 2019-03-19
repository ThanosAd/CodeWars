# Code for 'Snail' Kata - 4 Kyu
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snail(array):
    flag=1
    n=len(array)
    i=0
    j=0
    k=1
    result=[]
    if (len(array[0]))==0:
        return result
    for element in range(0,n**2):
    
        if flag==1:
            r=array[i][j]
            result.append(r)
            j=j+1
            if j==(n-k):
                flag=2
        elif flag==2:
            r=array[i][j]
            result.append(r)
            i=i+1
            if i==(n-k):
                flag=3
        elif flag==3:
            r=array[i][j]
            result.append(r)
            j=j-1
            if j==(-1+k):
                flag=4
        elif flag==4:
            r=array[i][j]
            result.append(r)
            i=i-1
            if i==(-1+k):
                flag=1
                k=k+1
                i=i+1
                j=j+1
    return result
