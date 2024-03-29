import numpy

## poly: returns the coefficients of a polynomial with the given sequence of roots.
# print(numpy.poly([-1, 1, 1, 10]))
# Output : [  1 -11   9  11 -10]

## roots: returns the roots of a polynomial with the given coefficients.
# print(numpy.roots([1, 0, -1]))
# Output : [-1.  1.]

## polyint: returns an antiderivative (indefinite integral) of a polynomial.
# print(numpy.polyint([1, 1, 1]))
# Output : [ 0.33333333  0.5         1.          0.        ]

## polyder: returns the derivative of the specified order of a polynomial.
# print(numpy.polyder([1, 1, 1, 1]))
# Output : [3 2 1]

## polyval: evaluates the polynomial at specific value.
# print(numpy.polyval([1, -2, 0, 2], 4))
# Output : 34

## polyfit: fits a polynomial of a specified order to a set of data using a least-squares approach.
# print(numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2))
# Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]

# The functions polyadd, polysub, polymul, and polydiv also handle proper addition, subtraction, multiplication, and division of polynomial coefficients, respectively.

a = list(map(float, input().split()))
b = int(input())

print(numpy.polyval(a, b))