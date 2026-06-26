class QNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = QNode(None)
        self.tail = QNode(None, self.head)
        self.head.next = self.tail

        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        prev = self.tail.prev

        newNode = QNode(value, prev, self.tail)

        prev.next = newNode
        self.tail.prev = newNode

        self.size += 1

    def appendleft(self, value: int) -> None:
        next = self.head.next

        newNode = QNode(value, self.head, next)

        self.head.next = newNode
        next.prev = newNode

        self.size += 1

    def pop(self) -> int:
        if self.size == 0: return -1

        target = self.tail.prev
        prev = target.prev

        prev.next = self.tail
        self.tail.prev = prev

        self.size -= 1

        return target.val

    def popleft(self) -> int:
        if self.size == 0: return -1

        target = self.head.next
        next = target.next

        self.head.next = next
        next.prev = self.head

        self.size -= 1

        return target.val
