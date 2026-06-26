class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= self.maxHeap[0] * -1: heapq.heappush(self.maxHeap, num * -1)
        else: heapq.heappush(self.minHeap, num)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)

        elif len(self.maxHeap) - len(self.minHeap) > 1:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)


    def findMedian(self) -> float:
        print(len(self.minHeap), len(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap): return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap): return self.maxHeap[0] * -1
        else:
            return (self.minHeap[0] + self.maxHeap[0] * -1) / 2