from typing import Deque

n = int(input())
dq = Deque()

for i in range(n):
    raw = input().split(" ")
    op = raw[0]

    if op == "pop":
        dq.pop()
    elif op == "popleft":
        dq.popleft()
    elif op == "append":
        dq.append(raw[1])
    elif op == "appendleft":
        dq.appendleft(raw[1])

print(" ".join(dq))