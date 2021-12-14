import numpy

## zeroes: returns a new array with a given shape and type filled with 0's.

# print numpy.zeros((1, 2))                    # Default type is float
# Output : [[ 0.  0.]]

# print numpy.zeros((1, 2), dtype = int) # Type changes to int
# Output : [[0 0]]

## ones: returns a new array with a given shape and type filled with 1's.

# print numpy.ones((1, 2))                    # Default type is float
# Output : [[ 1.  1.]]

# print numpy.ones((1, 2), dtype = int) # Type changes to int
# Output : [[1 1]]

a = list(map(int, input().split()))

print(numpy.zeros(a, dtype=int))
print(numpy.ones(a, dtype=int))
