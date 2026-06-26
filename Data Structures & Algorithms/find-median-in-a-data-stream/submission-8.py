class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if self.small and num < -1 * self.small[0]:
            heapq.heappush(self.small, -1 * num)
        else:
            heapq.heappush(self.big, num)

        if len(self.small) - len(self.big) > 1:
            heapq.heappush(self.big, -1 * heapq.heappop(self.small))
        elif len(self.big) - len(self.small) > 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) == len(self.big):
            return (-1 * self.small[0] + self.big[0]) / 2
        elif len(self.small) > len(self.big):
            return -1 * self.small[0]
        else:
            return self.big[0]
        
        