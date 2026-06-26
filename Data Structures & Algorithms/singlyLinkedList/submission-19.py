class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = None
    
    def get(self, index: int) -> int:
            node = self.head

            for i in range(index + 1):
                if node.next is None: return -1
                node = node.next
            
            return node.value

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        if self.tail == None: self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        if self.tail is None: self.insertHead(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        if self.head.next is None: return False

        prev = self.head
        current = self.head.next
        for i in range(index):
            if current.next is None: return False
            prev = current
            current = current.next
        prev.next = current.next
        if current.next == None:
            self.tail = prev
        return True

    def getValues(self) -> List[int]:
        node = self.head
        list = []

        while node.next is not None:
            node = node.next
            list.append(node.value)
        
        return list
