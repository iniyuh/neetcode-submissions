class Pair:

    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def hash(self, key: int):
        return key % self.capacity
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hashmap = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        if not self.hashmap[index]:
            self.hashmap[index] = Pair(key, value)
            self.size += 1
        else:
            prev = None
            curr = self.hashmap[index]
            while True:
                if not curr: 
                    prev.next = Pair(key, value)
                    self.size += 1
                    break
                elif curr.key == key: 
                    curr.value = value
                    break
                
                prev = curr
                curr = curr.next
        
        if self.size >= self.capacity // 2: self.resize()


    def get(self, key: int) -> int:
        index = self.hash(key)

        curr = self.hashmap[index]
        while True:
            if not curr: return -1
            elif curr.key == key: return curr.value

            curr = curr.next


    def remove(self, key: int) -> bool:
        index = self.hash(key)

        prev = None
        curr = self.hashmap[index]
        while True:
            if not curr: return False
            elif curr.key == key:
                if not prev: self.hashmap[index] = None
                else: prev.next = curr.next
                self.size -= 1
                return True
            
            prev = curr
            curr = curr.next

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        oldMap = self.hashmap
        self.hashmap = [None] * (2 * self.capacity)
        self.capacity *= 2
        self.size = 0

        for item in oldMap:
            if item:
                curr = item
                while curr:
                    self.insert(curr.key, curr.value)
                    curr = curr.next
    


