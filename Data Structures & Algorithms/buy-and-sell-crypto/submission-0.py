class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentProfit = 0
        currentMin = prices[0]
        for price in prices:
            profit = price - currentMin
            currentProfit = max(profit, currentProfit)
            currentMin = min(price, currentMin)
        
        return currentProfit