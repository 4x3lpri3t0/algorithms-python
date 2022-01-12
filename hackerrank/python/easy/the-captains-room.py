k = int(input())
numbers = list(map(int, input().split()))
rooms = set(numbers.copy())
seen = set()

for i in numbers:
    if i not in seen:
        seen.add(i)
    else:
        rooms.discard(i)

print(rooms.pop())

# Math alt:
# (sum(rooms) * k - sum(numbers)) / (k - 1)