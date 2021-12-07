from itertools import combinations

raw = input().split()

for i in range(1, int(raw[1]) + 1):
    for j in combinations(sorted(raw[0]), i):
        print(''.join(j))