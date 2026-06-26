class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.time = 0

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.cache[key][0] = self.time
            self.time += 1

            return self.cache[key][1]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key][0] = self.time
            self.cache[key][1] = value
            self.time += 1

        elif self.size < self.capacity:
            self.cache[key] = [self.time, value]
            self.time += 1
            self.size += 1

        else:
            minKey = None
            minTime = float('inf')

            for k, (t, v) in self.cache.items():
                if t < minTime: 
                    minKey = k
                    minTime = t
            
            del self.cache[minKey]
            self.size -= 1
            
            self.put(key, value)