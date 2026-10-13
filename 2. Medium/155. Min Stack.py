class MinStack:

    def __init__(self):
        self.s = []
        self.p = []

    def push(self, value: int) -> None:
        self.p.append(value)
        if len(self.s) == 0 or value <= self.s[-1]:
            self.s.append(value)

    def pop(self) -> None:
        temp = self.p.pop()
        if temp == self.s[-1]:
            self.s.pop()

    def top(self) -> int:
        return self.p[-1]

    def getMin(self) -> int:
        return self.s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
