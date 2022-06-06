# List:
# - Dynamically resized
# - Values can be deleted and inserted at arbitrary location
# - List comprehension: Powerful tool for instantiating arrays

import bisect
import copy
import math


A = [1] + [0] * 10
print(A)  # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Basic operations:

len(A)
A.append(42)
A.append(43)
A.remove(42)
A.insert(3, 28)

# Instantiate a 2d array:
array_2d = [[1, 2, 4], [3, 5, 7, 9], [13]]

# Checking if value is present (O(n)):
42 in A  # False

# Shallow copy:
A = [1, 2]
B = copy.copy(A)

# Deep copy:
A = [1, 2]
B = copy.deepcopy(A)  # Recursively inserts copies from the original object.

# Key methods:

min(A)
max(A)

# BS for sorted lists
bisect.bisect(A, 6)
bisect.bisect_left(A, 6)
bisect.bisect_right(A, 6)

A.reverse()  # in place
reversed(A)  # returns iterator
A.sort()  # in place
sorted(A)  # returns iterator

del A[0]  # deletes element at idx
del A[1:2]  # removes the slice


# Slicing examples
A = [0, 1, 2, 3, 4, 5, 6]
A[2:4]  # [2, 3] -> [index1, index2)
A[:4]  # [0, 1, 2, 3] -> Stop at 4th
A[:-1]  # [0, 1, 2, 3, 4, 5] -> All minus last (-1)
A[-3:]  # [4, 5, 6] -> All minus first three
A[-3:-1]  # [4, 5] -> All minus first three, then minus last
A[1:5:2]  # [1, 3] -> step 2
A[5:1:-1]  # [5, 4, 3, 2] -> [5th, 1st), right to left
A[5:1:-2]  # [5, 3] -> [5th, 1st), right to left, step 2
A[::-1]  # [6, 5, 4, 3, 2, 1, 0] -> Reverse

# Rotate a list:
k = 1
print(A[k:] + A[:k])  # rotates A by k to the left [1, 2, 3, 4, 5, 6, 0]

# List comprehension: Succint way to create lists that consists of
# (1.) input seq
# (2.) iterator over input seq
# (3.) logical condition over iterator (optional)
# (4.) expression that yields the elements of the derived list

[x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]

[x**2 for x in range(6) if x % 2 == 0]  # [0, 4, 16]

# List comprehensions can always be rewritten using map(), filter(), and lambdas
# ... but they're clearer to read (you avoid using lambdas explicitly)

# Multiple for loops:
A = [1, 3, 5]
B = ["a", "b"]

[
    (x, y) for x in A for y in B
]  # [(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]

# Convert a 2d list to a 1d list:
M = [[1, 2, 3], [4, 5, 6]]
[x for row in M for x in row]  # [1, 2, 3, 4, 5, 6]

# Two levels of looping also allow iterating over each entry in a 2d list:
A = [[1, 2, 3], [4, 5, 6]]
print([[x**2 for x in row] for row in M])  # [[1, 4, 9], [16, 25, 36]]

# Sets and dictionaries also support list comprehensions
