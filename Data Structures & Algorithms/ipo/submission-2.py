class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCost = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCost)

        for _ in range(k):
            while minCost and minCost[0][0] <= w:
                p = heapq.heappop(minCost)[1]
                heapq.heappush(maxProfit, -1 * p)

            if not maxProfit: break

            w += -1 * heapq.heappop(maxProfit)
        
        return w