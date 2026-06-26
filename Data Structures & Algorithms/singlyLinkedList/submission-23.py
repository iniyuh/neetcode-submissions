class Node:
    def __init__(self, val, right=None):
        self.val = val
        self.right = right


class LinkedList:
    
    def __init__(self):
        self.root = None
    
    def get(self, index: int) -> int:
        node = self.root
        i = 0
        while node:
            if i == index: return node.val
            node = node.right
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        self.root = Node(val, self.root)

    def insertTail(self, val: int) -> None:
        if not self.root: 
            self.root = Node(val)
            return

        curr = self.root
        while curr.right: curr = curr.right
        curr.right = Node(val)

    def remove(self, index: int) -> bool:
        if index == 0: 
            if self.root: 
                self.root = self.root.right
                return True
            else: return False

        prev, curr = None, self.root
        i = 0
        while curr:
            if i == index: 
                prev.right = curr.right 
                return True
            if i > index: return False
            prev = curr
            curr = curr.right
            i += 1
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.root
        while curr:
            res.append(curr.val)
            curr = curr.right
        return res
        
