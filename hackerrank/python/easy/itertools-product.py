from itertools import product

A = map(int, input().split())
B = map(int, input().split())

print(*list(product(A, B)))