def gaussSeidel(A, b, error):  # n=3
    # Assume A is diagonally dominant, or that gauss seidel will converge.

    x1_prev = 0
    x2_prev = 0
    x3_prev = 0

    e1 = 1000
    e2 = 1000
    e3 = 1000

    while (e1 & e2 & e3 < error):
        x1 = A[1, 1] = (b[1]-x2_prev*A[1, 2] - x3_prev*A[1, 3])/A[1, 1]
        e1 = (x1_prev - x1)/x1
        x1_prev = x1
        x2 = A[2, 2] = (b[2]-x1_prev*A[2, 1] - x3_prev*A[2, 3])/A[2, 2]
        e2 = (x2_prev - x2)/x2
        x2_prev = x2
        x3 = A[3, 3] = (b[3]-x1_prev*A[3, 1] - x2_prev*A[3, 2])/A[3, 3]
        e3 = (x3_prev - x3)/x3
        x3_prev = x3
    return x1, x2, x3
