# Stack with constant getMin() time
class MinStack:
    def __init__(self):
        # Each element in the stack will be a tuple, (x, y). x is value, y is min value at the time.
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x, x))

    def pop(self) -> None:
        if not self.stack:
            return None

        popped = self.stack.pop()
        return popped

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]


# MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# top_value = obj.top()
# min_value = obj.getMin()
obj = MinStack()
print(obj.push(2))
print(obj.push(3))
print(obj.pop())
print(obj.top())
print(obj.push(1))
print(obj.push(100))
print(obj.getMin())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
