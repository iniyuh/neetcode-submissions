class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Deque:
    
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self) -> bool:
        return self.front is None

    def append(self, value: int) -> None:
        if self.front is None:
            self.front = Node(value)
            self.back = self.front
        else:
            self.back.right = Node(value, self.back)
            self.back = self.back.right

    def appendleft(self, value: int) -> None:
        if self.front is None:
            self.front = Node(value)
            self.back = self.front
        else:
            self.front.left = Node(value, None, self.front)
            self.front = self.front.left

    def pop(self) -> int:
        if self.front is None: return -1
        else:
            val = self.back.val
            self.back = self.back.left
            if self.back is None: self.front = None
            else: self.back.right = None
            return val

    def popleft(self) -> int:
        if self.front is None: return -1
        else:
            val = self.front.val
            self.front = self.front.right
            if self.front is None: self.back = None
            else: self.front.left = None
            return val
