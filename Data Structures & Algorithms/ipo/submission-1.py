class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        self.profFromCap = defaultdict(list)

        for i in range(len(profits)):
            heapq.heappush(self.profFromCap[capital[i]], -1 * profits[i])
        

        for _ in range(k):
            winningCost = 0
            maxProfit = 0

            for c in range(w + 1):
                if self.profFromCap[c] and -1 * self.profFromCap[c][0] > maxProfit:
                    winningCost = c
                    maxProfit = -1 * self.profFromCap[c][0]
            
            if maxProfit == 0: return w

            w += maxProfit
            heapq.heappop(self.profFromCap[winningCost])

        return w

            