import numpy

## dot product:
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.dot(A, B)       #Output : 11

## cross product:
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.cross(A, B)     #Output : -2

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(a, b))