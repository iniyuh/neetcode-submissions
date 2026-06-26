class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size: return -1

        node = self.head
        i = 0

        while i < index:
            node = node.next
            i += 1
        
        return node.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val)

        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = self.tail = newNode
        
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)

        if self.tail: 
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode
        
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size: return False

        if index == 0:
            self.head = self.head.next
        else:
            i = 0
            node = self.head
            while i < index - 1: 
                node = node.next
                i += 1
            previousNode = node
            nextNode = node.next.next
            previousNode.next = nextNode

            if nextNode is None: self.tail = previousNode

        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        arr = []

        node = self.head
        while node: 
            arr.append(node.val)
            node = node.next

        return arr
        
