from typing import List


class Queue:
    def __init__(self) -> None:
        self._enq: List[int] = []
        self._deq: List[int] = []

    # Added for testing
    def __str__(self):
        return (
            "Enq stack: "
            + " ".join(str(elem) for elem in self._enq)
            + "\nDeq stack: "
            + " ".join(str(elem) for elem in self._deq)
        )

    def enqueue(self, x: int) -> None:
        self._enq.append(x)

    def dequeue(self) -> int:
        if not self._deq:
            # Transfers the elements in _enq to _deq.
            while self._enq:
                self._deq.append(self._enq.pop())
        return self._deq.pop()


# TODO: Validate
q = Queue()
print(q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)  # 1, 2, 3
print(q.dequeue())  # 1
print(q)  # 3, 2
q.enqueue(4)
print(q)  # 4 # 3, 2
print(q.dequeue())
