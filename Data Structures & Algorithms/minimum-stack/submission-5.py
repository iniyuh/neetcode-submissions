class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = None

    def push(self, val: int) -> None:
        if self.min_ is not None: self.min_ = min(self.min_, val)
        else: self.min_ = val

        print(self.min_)

        self.stack.append((val, self.min_))

    def pop(self) -> None:
        top_val = self.stack.pop()[0]
        if top_val == self.min_: 
            if self.stack: self.min_ = self.stack[-1][1]
            else: self.min_ = None

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
