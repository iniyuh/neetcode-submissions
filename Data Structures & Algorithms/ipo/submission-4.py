class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        maxHeap = []

        for i in range(len(profits)):
            heapq.heappush(minHeap, (capital[i], profits[i]))
        
        count = 0
        while count < k:
            while minHeap and minHeap[0][0] <= w:
                heapq.heappush(maxHeap, -1 * heapq.heappop(minHeap)[1])

            if not maxHeap: break

            w -= heapq.heappop(maxHeap)

            count += 1
        
        return w