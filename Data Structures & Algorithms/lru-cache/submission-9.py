class Node: 
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hm = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAtTail(self, node: Node) -> None:
        self.tail.prev.next = node
        node.prev = self.tail.prev

        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def moveToTail(self, key: int) -> None:
        node = self.hm[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

        self.insertAtTail(node)
    
    def removeOldest(self) -> None:
        node = self.head.next

        node.next.prev = self.head
        self.head.next = node.next
        
        del self.hm[node.key]
        self.size -= 1


    def get(self, key: int) -> int:
        if key in self.hm:
            self.moveToTail(key)
            return self.hm[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.moveToTail(key)
            self.hm[key].val = value
        else:
            node = Node(key, value)
            self.hm[key] = node
            self.insertAtTail(node)

            if self.size > self.capacity:
                self.removeOldest()


        
