from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())

# Input
for i in range(n):
    word = input()
    d[word].append(str(i + 1))

# Output
for i in range(m):
    word = input()
    print(' '.join(d[word]) or -1)