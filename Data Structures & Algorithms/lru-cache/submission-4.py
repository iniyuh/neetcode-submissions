class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.timestamp = 0
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key in self.hashmap: 
            self.timestamp += 1
            self.hashmap[key][1] = self.timestamp
            return self.hashmap[key][0]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap and self.size == self.capacity:
            min_key = min(self.hashmap, key=lambda k: self.hashmap[k][1])
            print("Deleted: [", min_key, ", ", self.hashmap[min_key][0], "] with timestamp: ", self.hashmap[min_key][1])
            del self.hashmap[min_key]
            self.size -= 1

        if key not in self.hashmap: self.size += 1
        self.timestamp += 1
        self.hashmap[key] = [value, self.timestamp]
        # print("Put ", key, ", timestamp: ", self.timestamp)

