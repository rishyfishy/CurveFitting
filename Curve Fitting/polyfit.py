def naiveGaussJordan(matrix: list, vector: list):
    n = len(matrix)
    newMat = matrix.copy()
    newVec=vector.copy()
    # Forward Propogation
    for k in range(n-1):    #every diagonal element except last

        for i in range(k+1, n):     #every row below the k'th diagonal element
            factor = newMat[i][k]/newMat[k][k]
            for j in range(k, n):

                newMat[i][j] -= factor*newMat[k][j]

            newVec[i] -= factor*newVec[k]
    # Back-substitution
    x = n*[0]
    # x[n-1] = newVec[n-1]/newMat[n-1][n-1]

    for i in reversed(range(n)):
        sum = newVec[i]
        for j in range(i+1, n):
            sum -= newMat[i][j]*x[j]
        x[i] = sum/newMat[i][i]

    return x
    
def polyfit(x,y):
    '''
    returns a list of coefficients _a_ in the order a0 + a1*x + a2*x^2 +a3*x^3+...
    Output will always be a list of numbers with a length of len(x)
    '''
    n=len(x)-1

    A=[[x[i]**j for j in range (n+1)] for i in range (n+1)]
    #TODO: Warn if matrix is ill conditioned.
    a=naiveGaussJordan(A,y)
    return a

print(polyfit([0,2,3],[0,0,0]))

