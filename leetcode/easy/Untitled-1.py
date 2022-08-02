from ast import For
import numpy as np

A = np.arange(100.0)
splittedA = np.split(A, 10)

B = np.arange(100.0)
splittedB = np.split(B, 10)

# (A - B) / (C - D)

i = 0
for i in range(len(splittedA)):
    result = splittedA[i] - splittedB[i]
    print(result)
