class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Deque:
    
    def __init__(self):
        self.empty = True
        self.L = None
        self.R = None

    def isEmpty(self) -> bool:
        return self.empty

    def append(self, value: int) -> None:
        node = Node(value)

        if self.empty:
            self.L = self.R = node
            self.empty = False
        else:
            self.R.right = node
            node.left = self.R
            self.R = node


    def appendleft(self, value: int) -> None:
        node = Node(value)

        if self.empty:
            self.L = self.R = node
            self.empty = False
        else:
            node.right = self.L
            self.L.left = node
            self.L = node

    def pop(self) -> int:
        if self.empty: return -1

        val = self.R.val
        newR = self.R.left

        if newR is None:
            self.empty = True
            self.L = self.R = None
        else:
            self.R = newR
            self.R.right = None
        
        return val
        

    def popleft(self) -> int:
        if self.empty: return -1

        val = self.L.val

        newL = self.L.right

        if newL is None:
            self.empty = True
            self.L = self.R = None
        else:
            self.L = newL
            self.L.left = None
        
        return val
        
