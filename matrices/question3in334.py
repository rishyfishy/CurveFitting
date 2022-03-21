from thomasAlgo import thomas
from LUDecomposition import eye

for j in range(1, 71):
    A = [[5, -8, 0, 0],
         [-5, 10*j+8, -8, 0],
         [0, -10*j, 34, -10],
         [0, 0, -15, 10]]
    b = [3, 0, 0, 6]
    identiy, x = thomas(A, b)
    if (abs(x[1]-0.02)<0.0002):
        print (j)
        print('\n')
        print(x)
