from itertools import combinations_with_replacement

a = input().split()
for i in sorted(combinations_with_replacement(sorted(a[0]), int(a[1]))):
    print("".join(i))