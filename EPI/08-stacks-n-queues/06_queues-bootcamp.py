# Basic queue API + max method:

import collections
from typing import Deque


class Queue:
    def __init__(self) -> None:
        self._data: Deque[int] = collections.deque()

    def enqueue(self, x: int) -> None:
        self._data.append(x)

    def dequeue(self) -> int:
        return self._data.popleft()

    def max(self) -> int:
        return max(self._data)

    # Added for testing
    def __str__(self):
        return " ".join(str(datum) for datum in self._data)


# Validation:
q = Queue()
q.enqueue(1)
print(q)
print("Max: " + str(q.max()))
q.enqueue(2)
print(q)
print("Max: " + str(q.max()))
q.dequeue()
print(q)


# For problems that don't require to implement your own queue class; use the `collections.deque` class.
# q.append(e)
# q[0]
# q.popleft()
