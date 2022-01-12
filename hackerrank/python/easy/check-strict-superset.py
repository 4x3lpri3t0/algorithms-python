A = set(input().split())
n = int(input())

sss = True

for i in range(n):
    s = set(input().split())

    if (len(A) == len(s)) or (not A.issuperset(s)):
        sss = False
        break

print(sss)
