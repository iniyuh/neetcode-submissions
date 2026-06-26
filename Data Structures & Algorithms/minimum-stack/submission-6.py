class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        currentMin = self.arr[-1][1] if self.arr else float('inf')
        self.arr.append( (val, min(val, currentMin)) )

    def pop(self) -> None:
        return self.arr.pop()[0]

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:
        return self.arr[-1][1]
