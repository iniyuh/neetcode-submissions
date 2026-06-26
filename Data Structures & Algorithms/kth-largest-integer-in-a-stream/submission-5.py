class KthLargest:
    def swap(self, i, j):
        temp = self.minHeap[i]
        self.minHeap[i] = self.minHeap[j]
        self.minHeap[j] = temp

    def push(self, val: int) -> None:
        self.minHeap.append(val)
        i = len(self.minHeap) - 1

        while i // 2 > 0:
            if self.minHeap[i] < self.minHeap[i // 2]:
                self.swap(i, i // 2)
                i = i // 2
            else: break
    
    def pop(self) -> None:
        if len(self.minHeap) == 1: return

        self.swap(1, len(self.minHeap) - 1)
        self.minHeap.pop()
        i = 1

        while 2 * i < len(self.minHeap):
            lessRight = self.minHeap[i] > self.minHeap[2*i+1] if 2*i+1 < len(self.minHeap) else False
            if self.minHeap[i] > self.minHeap[2*i] and lessRight:
                if self.minHeap[2*i] < self.minHeap[2*i+1]:
                    self.swap(i, 2*i)
                    i = 2*i
                else:
                    self.swap(i, 2*i+1)
                    i = 2*i+1
            elif self.minHeap[i] > self.minHeap[2*i]:
                self.swap(i, 2*i)
                i = 2*i
            elif lessRight:
                self.swap(i, 2*i+1)
                i = 2*i+1
            else: break


    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [0]
        self.k = k

        for num in nums:
            self.push(num)
        
        while len(self.minHeap) - 1 > k:
            self.pop()
        
        print("Initial: ", self.minHeap)



    def add(self, val: int) -> int:
        self.push(val)
        if len(self.minHeap) - 1 > self.k: self.pop()
        print("Added ", val, ":", self.minHeap)
        return self.minHeap[1]
