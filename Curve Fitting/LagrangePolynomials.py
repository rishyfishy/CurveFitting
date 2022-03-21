def LagrangePolyFit(x:list,y:list,xint:float or int):
    '''
    finds the polynomial fit using the 
    Lagrange method
    '''
    n=len(x)
    product =(n+1)*[1.0]
    for i in n:
        for j in n:
            if i==j:
                pass
            L[i]*=1

    sum=0
    for i in range(n+1):
        product[i]=y[i]
        for j in range(n+1):
            if i==j:
                pass
            product*= ()
