m = int(input())
M = set(input().split())
n = int(input())
N = set(input().split())

sorted_intersection = sorted(N ^ M, key=int)

print("\n".join(sorted_intersection))