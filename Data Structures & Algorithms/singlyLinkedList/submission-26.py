class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.root = LinkedListNode(None)
    
    def get(self, index: int) -> int:
        i = 0
        node = self.root.next

        while node and i < index:
            node = node.next
            i += 1
        
        return node.val if node else -1

    def insertHead(self, val: int) -> None:
        newNode = LinkedListNode(val, self.root.next)
        self.root.next = newNode

    def insertTail(self, val: int) -> None:
        node = self.root
        while node.next: node = node.next
        node.next = LinkedListNode(val)

    def remove(self, index: int) -> bool:
        prev = self.root
        curr = self.root.next
        i = 0

        while i < index and curr:
            prev = curr
            curr = curr.next
            i += 1
        
        if curr:
            prev.next = curr.next
            curr.next = None
            return True
        else: return False


    def getValues(self) -> List[int]:
        ret = []
        curr = self.root.next

        while curr:
            ret.append(curr.val)
            curr = curr.next
        
        return ret
        
