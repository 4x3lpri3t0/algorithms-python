n = int(input())
a = list(map(int, input().split()))

lookup = [0] * n
for i in range(n):
    lookup[a[i] - 1] = i + 1

m = int(input())
b = list(map(int, input().split()))

l, r = 0, 0
for i in range(m):
    l += lookup[b[i] - 1]
    r += n - lookup[b[i] - 1] + 1

print(f"{l} {r}")