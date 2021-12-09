a = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

# Difference
print(len(A - B))

# Symmetric difference
print(len(A ^ B))

# Intersection
print(len(A & B))

# Union
print(len(set.union(A, B)))