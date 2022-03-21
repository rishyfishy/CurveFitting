def threetwo(n: int):
    # n is the number of segments

    twos = -n % 3
    threes = (n-2*twos)//3

    return threes, twos

# print(threetwo(2))
# print(threetwo(3))
# print(threetwo(13))

# (0, 1)
# (1, 0)
# (3, 2)
