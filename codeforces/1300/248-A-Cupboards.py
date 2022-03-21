n = int(input())
r = 0
l = 0
for i in range(n):
    a, b = map(int, input().split())
    l += a
    r += b

l = min(l, n - l)
r = min(r, n - r)
print(r + l)