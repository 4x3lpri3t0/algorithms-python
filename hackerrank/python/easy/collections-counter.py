from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))
n = int(input())

money_earned = 0
for i in range(1, n + 1):
    size, price = map(int, input().split())

    if (sizes[size] > 0):
        sizes[size] -= 1
        money_earned += price

print(money_earned)