class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        for price in prices[1:]:
            if price < minPrice: minPrice = price
            elif price > minPrice: profit = max(profit, price - minPrice)
        
        return profit
        
"""

This is possible in O(1) by iterating through the array once.

Profit is = sellPrice - buyPrice

So we want to minimize buyPrice and maximize sellPrice from our prices array
while maintaining order.

On any given day IF a profit can be turned, we know that maximum profit possible by keeping track
of minimum price so far.

Time and space are O(1)

Test cases:
 0 1 2 3 4 5 = 5
 0 1 2 3 1 0 = 3
 5 4 3 2 1 0 = 0
 6 9 8 4 10 = 6

"""