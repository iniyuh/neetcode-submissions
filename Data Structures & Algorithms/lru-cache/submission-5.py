class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.size = 0
        self.q = deque()

    def get(self, key: int) -> int:
        if key in self.hm: 
            self.q.remove(key)
            self.q.append(key)
            return self.hm[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.q.remove(key)
            self.q.append(key)
            self.hm[key] = value
        else:
            self.hm[key] = value
            self.q.append(key)

            if self.size == self.capacity:
                deleteKey = self.q.popleft()
                del self.hm[deleteKey]
            else: self.size += 1
        
