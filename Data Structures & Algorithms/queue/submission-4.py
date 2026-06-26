class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Deque:
    
    def __init__(self):
        self.left = self.right = None

    def isEmpty(self) -> bool:
            return self.left is None

    def append(self, value: int) -> None:
        if not self.left: self.left = self.right = Node(value)
        else:
            self.right.right = Node(value, self.right, None)
            self.right = self.right.right

    def appendleft(self, value: int) -> None:
        if not self.left: self.left = self.right = Node(value)
        else:
            self.left.left = Node(value, None, self.left)
            self.left = self.left.left
        

    def pop(self) -> int:
        if not self.left: return -1

        val = self.right.val
        self.right = self.right.left
        if self.right: self.right.right = None
        else: self.left = None
        return val
        

    def popleft(self) -> int:
        if not self.left: return -1

        val = self.left.val
        self.left = self.left.right
        if self.left: self.left.left = None
        else: self.right = None
        return val