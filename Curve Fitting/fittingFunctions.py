import math
import matplotlib.pyplot as plt
import random


def naiveGaussJordan(matrix: list, vector: list):
    n = len(matrix)
    newMat = matrix.copy()
    # Forward Propogation
    for k in range(n-1):  # every diagonal element except last

        for i in range(k+1, n):  # every row below the k'th diagonal element
            factor = newMat[i][k]/newMat[k][k]
            for j in range(k, n):

                newMat[i][j] -= factor*newMat[k][j]

            vector[i] -= factor*vector[k]
    # Back-substitution
    x = n*[0]
    # x[n-1] = vector[n-1]/newMat[n-1][n-1]

    for i in reversed(range(n)):
        sum = vector[i]
        for j in range(i+1, n):
            sum -= newMat[i][j]*x[j]
        x[i] = sum/newMat[i][i]

    return x
# x=list(range(1,11))
# y=[3*4**xi+(-1+2*random.random()) for xi in x]
# print(powerLawFit(x,y))


def linearFit(x, y):
    '''
    Uses least squares method to perform a linear fit on the data
    '''
    n = len(x)
    X = 0.0
    Y = 0.0
    XY = 0.0
    X2 = 0.0
    Y2 = 0.0
    for i in range(len(x)):
        X += x[i]
        Y += y[i]
        XY += x[i]*y[i]
        X2 += x[i]**2
        Y2 += y[i]**2

    a = (n*XY-X*Y)/(n*X2-X**2)
    b = Y/n-a*X/n
    return a, b


def polynomialFit(x, y, m=2):
    '''
    returns a list of coefficients _a_ in the order a0 + a1*x + a2*x^2 +a3*x^3
    Assumes quadratic fit (m=2) if m is not specified
    Output will always be a list of numbers with a length of (m+1)
    '''
    A = [[sum([xi**(m1+m2) for xi in x]) for m1 in range(m+1)]
         for m2 in range(m+1)]
    b = [sum([x[i]**m1*y[i] for i in range(len(x))]) for m1 in range(m+1)]
    a = naiveGaussJordan(A, b)
    return a


# x = [3,4,5,7,8]
# y = [1.6,3.6,4.4,3.4,2.2]
# print(polynomialFit(x, y))


def powerLawFit(x, y):
    '''
    returns α and β respectively in the equation 
    y= β*x^α
    '''
    lny = [math.log(yi) for yi in y]
    lnx = [math.log(xi) for xi in x]
    a, b = linearFit(lnx, lny)

    return a, math.exp(b)

# x=list(range(1,11))
# y=[3*xi**4 for xi in x]
# print(powerLawFit(x,y))


def exponentialFit(x, y):
    '''
    returns α and β respectively in the equation 
    y= βe^(αx)
    '''
    lny = [math.log(yi) for yi in y]
    a, b = linearFit(x, lny)

    return a, math.e**b

# x=list(range(1,11))
# y=[3*math.exp(4*xi)+(-1+2*random.random()) for xi in x]
# print(exponentialFit(x,y))


def saturationFit(x, y):
    '''
    returns α and β respectively in the equation 
         α x
    y= -------
        x + β
    '''
    invx = [1/xi for xi in x]
    invy = [1/yi for yi in y]
    b, a = linearFit(invx, invy)

    return 1/a, b/a


# x = list(range(1, 11))
# y = [3*xi/(xi+4) for xi in x]
# print(saturationFit(x, y))

print("Successfully imported fittingFunctions")

def MultipleLinearRegression(x,y):
    '''
    returns a list of coefficients _a_ in the order a0 + a1*x + a2*y +a3*z
    Output will always be a list of numbers with a length of (len(x)+1)
    '''
    dim=len(x)
    n=len(x[1])
    x=[n*[1]]+x
    A = [[sum([xi[k]*xj[k] for k in range(n)]) for xj in x]
         for xi in x]
    b = [sum([x[i][k]*y[k] for k in range(n)]) for i in range(dim+1)]
    a = naiveGaussJordan(A, b)
    return a

x=[[0,0,1,1],[0,1,0,1]]
y=[1,2,3,4]
print("Hello world")
print(MultipleLinearRegression(x,y))

def multiPower(x,y):
    lny= [math.log(yi) for yi in y]
    lnx=[[math.log(xi) for xi in x[i]]for i in range(len(x))]
    a = MultipleLinearRegression(lnx,lny)


def multiExponential(x,y):
    lny= [math.log(yi) for yi in y]
