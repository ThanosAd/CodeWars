def matrixMultiplication2x2(a,b):
    
    c = [0,0,0,0]
    c[0] = a[0]*b[0]+a[1]*b[2]
    c[1] = a[0]*b[1]+a[1]*b[3]
    c[2] = a[2]*b[0]+a[3]*b[2]
    c[3] = a[2]*b[1]+a[3]*b[3]
    
    return c

def fib(exp):
    
    base=[1,1,1,0]
    if exp<0:
        result1=1
        result0=0
        result=0
        
        for i in range(0,exp,-1):
            result = result1-result0
            result1=result0
            result0=result
        
        return result

    result = [1,1,1,0]
    
    while exp>0:
        if exp%2==1:
            result = matrixMultiplication2x2(result,base)
        base=matrixMultiplication2x2(base,base)
        exp=exp//2
    return result[3]
