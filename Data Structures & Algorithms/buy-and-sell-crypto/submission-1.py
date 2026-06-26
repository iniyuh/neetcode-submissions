class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        prevMin = prices[0]

        for price in prices:
            maxProf = max(maxProf, price - prevMin)
            prevMin = min(prevMin, price)
        
        return maxProf