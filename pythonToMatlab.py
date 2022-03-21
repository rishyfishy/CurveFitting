myString='''
def polynomialFit(x, y, m=2):
    ''
    returns a list of coefficients _a_ in the order a0 + a1*x + a2*x^2 +a3*x^3
    Assumes quadratic fit (m=2) if m is not specified
    Output will always be a list of numbers with a length of (m+1)
    ''
    A = [[sum([xi**(m1+m2) for xi in x]) for m1 in range(m+1)]
         for m2 in range(m+1)]
    b = [sum([x[i]**m1*y[i] for i in range(len(x))]) for m1 in range(m+1)]
    a = naiveGaussJordan(A, b)
    return a
'''
myDict={'**':'^',
'def':'function =', 
' in range (':'=1:', 
'math.log':'log',
'math.e':'exp(',
'#':'%',
'len':'length',
'],[':';',
'[':'(',
']':')'
}#
for key in myDict:
    myString=myString.replace(key,myDict[key])
print(myString)
