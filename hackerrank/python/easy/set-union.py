a = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))

print(len(set.union(A, B)))