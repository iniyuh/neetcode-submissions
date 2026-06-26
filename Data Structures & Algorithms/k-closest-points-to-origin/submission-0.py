class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [[math.sqrt(point[0] ** 2 + point[1] ** 2), point[0], point[1]] for point in points]
        heapq.heapify(arr)

        ret = []
        for i in range(k):
            temp = heapq.heappop(arr)
            ret.append([temp[1], temp[2]])

        return ret