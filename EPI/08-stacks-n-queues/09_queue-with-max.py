import collections
from typing import Any, Deque


class QueueWithMax:
    def __init__(self):
        self._entries: Deque[Any] = collections.deque()
        self._candidates_for_max: Deque[Any] = collections.deque()

    def enqueue(self, x):
        self._entries.append(x)
        # Eliminate dominated elements in _candidates_for_max.
        while self._candidates_for_max and self._candidates_for_max[-1] < x:
            self._candidates_for_max.pop()
        self._candidates_for_max.append(x)

    def deque(self):
        result = self._entries.popleft()
        if result == self._candidates_for_max[0]:
            self.candidates_for_max.popleft()
        return result

    def max(self):
        return self._candidates_for_max[0]


# TODO: Review + Validate
