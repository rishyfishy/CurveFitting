def eye(n):
    # Returns an n*n identity matrix
    mat = [n*[0] for i in range(n)]
    for i in range(n):
        mat[i][i] = 1
    return mat


def LU(matrix: list):
    # Performs LU decomposition on a square matrix
    n = len(matrix)
    U = matrix.copy()
    L = eye(n)
    # Forward Propogation
    for k in range(n-1):  # every diagonal element except last

        for i in range(k+1, n):  # every row below the k'th diagonal element
            factor = U[i][k]/U[k][k]
            L[i][k] = factor
            for j in range(k, n):

                U[i][j] -= factor*U[k][j]
    return L, U

# %%

def LURound(matrix: list, decimals: int):
    '''
    Performs LU decomposition on a square matrix

    inputs: 
        matrix: system matrix
        decimals: decimals of rounding
    outputs:
        L and U matrices
    '''
    n = len(matrix)
    U = [[round(number, decimals) for number in row] for row in matrix]
    L = eye(n)
    # Forward Propogation
    for k in range(n-1):  # every diagonal element except last

        for i in range(k+1, n):  # every row below the k'th diagonal element
            factor = round(U[i][k]/U[k][k], decimals)
            L[i][k] = factor
            for j in range(k, n):

                U[i][j] -= round(factor*U[k][j], decimals)
    return L, U

# TODO: Modify this for LU
def partialPivoting(matrix: list, vector: list) -> list:
    n = len(vector)
    x = n*[0]

    for k in range(1, n):
        # Swap the first row and the row with max first element

       # zero out first column
        for i in range(k+1, n+1):
            factor = matrix[i, k]/matrix[k, k]

            for j in range(k+1, n+1):
                matrix[i, j] -= factor*matrix[k, j]


print(eye(4))
a = [[2,-1,3], [-2,-2,-2], [2,-7,4]]
b, c = LU(a)
print(b)
print(c)

# # %%
