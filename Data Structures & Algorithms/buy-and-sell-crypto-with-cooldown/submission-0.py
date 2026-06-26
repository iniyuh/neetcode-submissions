class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buyPrice):
            if i >= len(prices): return 0
            elif (i, buyPrice) in memo: return memo[(i, buyPrice)]
            else:
                if buyPrice == -1:
                    memo[(i, buyPrice)] =  max( dfs(i+1, -1), dfs(i+1, prices[i]) - prices[i] )
                else:
                    memo[(i, buyPrice)] = max( dfs(i+1, buyPrice), dfs(i+2, -1) + prices[i] )

                return memo[(i, buyPrice)]
        
        return dfs(0, -1)