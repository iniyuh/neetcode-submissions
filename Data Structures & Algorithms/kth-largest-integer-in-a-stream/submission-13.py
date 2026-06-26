class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        
        while len(self.minHeap) > k: heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            return self.minHeap[0]
        else:
            if val > self.minHeap[0]:
                heapq.heappush(self.minHeap, val)
                heapq.heappop(self.minHeap)
            return self.minHeap[0]