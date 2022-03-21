def thomas(matrix, vector):
    '''
    function that solves tridiagonal systems of equations
    inputs:
        matrix: a square matrix describing the system _A_
        vector: the input vector _x_
    '''
    matrixCopy = [v.copy()for v in matrix]
    vectorCopy = vector.copy()
    forMatrix, forVector = forwardPropogate(matrixCopy, vectorCopy)
    eyemat, answer = backSubstitute(forMatrix, forVector)
    return eyemat, answer


def forwardPropogate(matrix, vector):
    '''
    Forward propogation step of thomas algorithm
    '''
    matrixCopy = [v.copy()for v in matrix]
    vectorCopy = vector.copy()
    # Forward propogation
    for i in range(len(vector)-1):  # all except last row
        # Divide row by diagonal value
        matrixCopy[i][i+1] /= matrixCopy[i][i] #g
        vectorCopy[i] /= matrixCopy[i][i] #r
        # matrixCopy[i][i] = 1

        # Subtract row i from next row
        matrixCopy[i+1][i+1] -= matrixCopy[i+1][i]*matrixCopy[i][i+1]
        vectorCopy[i+1] -= matrixCopy[i+1][i]*vectorCopy[i]
        # matrixCopy[i+1][i] = 0

    # Divide last row by diagonal value
    i = len(vectorCopy)-1
    vectorCopy[i] /= matrixCopy[i][i]
    # matrixCopy[i][i] = 1
    return matrixCopy, vectorCopy


def backSubstitute(matrix, vector):
    '''
    Back substitution step of thomas algorithm
    '''
    # Back-substitution
    matrixCopy = matrix.copy()
    vectorCopy = vector.copy()
    for i in reversed(range(len(vector)-1)):
        vectorCopy[i] -= matrix[i][i+1]*vectorCopy[i+1]
        matrixCopy[i][i+1] = 0
    return matrixCopy, vectorCopy


# A = [[5, -8, 0, 0],
#         [-5, 18, -8, 0],
#         [0, -10, 34, -10],
#         [0, 0, -15, 10]]
# b = [3, 0, 0, 6]
# c,d=thomas(A,b)
