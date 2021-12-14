# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

# Use the transpose and flatten tools in the NumPy module to manipulate an array.

import numpy

n, m = map(int, input().split())

M = numpy.array([input().split() for i in range(n)], int)

print(M.transpose())
print(M.flatten())
