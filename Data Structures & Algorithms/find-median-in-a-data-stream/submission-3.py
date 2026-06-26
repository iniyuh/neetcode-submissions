class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num < self.minHeap[0]: 
            heapq.heappush(self.maxHeap, -1 * num)
        else:                       
            heapq.heappush(self.minHeap, num)

        MIN, MAX = len(self.minHeap), len(self.maxHeap)

        if MIN - MAX > 1:
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
        elif MAX - MIN > 1:
            heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        MIN, MAX = len(self.minHeap), len(self.maxHeap)

        if MIN > MAX: return self.minHeap[0]
        elif MAX > MIN: return -1 * self.maxHeap[0]
        else: return (self.minHeap[0] - self.maxHeap[0])/2
        
        