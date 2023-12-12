class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)
        

    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
    

ms = MinStack()

ms.push(1)
assert ms.top() == 1
assert ms.getMin() == 1

ms.push(5)
assert ms.top() == 5
assert ms.getMin() == 1

ms.pop()
assert ms.top() == 1
assert ms.getMin() == 1
print("passed")