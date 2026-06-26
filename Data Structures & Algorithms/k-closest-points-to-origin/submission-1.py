class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distFromOrigin(self):
        return self.x ** 2 + self.y ** 2
    
    def toArr(self):
        return [self.x, self.y]
    
    def __lt__(self, other):
        return self.distFromOrigin() < other.distFromOrigin()

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        custArr = []

        for x, y in points:
            custArr.append(Point(x, y))
        
        heapq.heapify(custArr)

        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(custArr).toArr())
        
        return ret
        