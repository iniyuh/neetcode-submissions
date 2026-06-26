class MedianFinder:

    def __init__(self):
        self.maxH = []
        self.minH = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxH, -1 * num)

        if self.minH and -1 * self.maxH[0] > self.minH[0]:
            num1, num2 = -1 * heapq.heappop(self.maxH), -1 * heapq.heappop(self.minH)
            heapq.heappush(self.maxH, num2)
            heapq.heappush(self.minH, num1)
        
        if len(self.maxH) - len(self.minH) > 1:
            heapq.heappush(self.minH, -1 * heapq.heappop(self.maxH))
        elif len(self.minH) - len(self.maxH) > 1:
            heapq.heappush(self.maxH, -1 * heapq.heappop(self.minH))


        print("Adding", num)
        print("minheap:", self.minH)
        print("maxheap:", self.maxH * -1)
        

    def findMedian(self) -> float:
        if len(self.minH) < len(self.maxH): return -1 * self.maxH[0]
        elif len(self.maxH) < len(self.minH): return self.minH[0]
        else: return (-1 * self.maxH[0] + self.minH[0])/2
        