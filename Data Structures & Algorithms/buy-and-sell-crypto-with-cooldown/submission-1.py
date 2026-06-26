class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buying):
            if i >= len(prices): return 0
            elif (i, buying) in memo: return memo[(i, buying)]
            else:
                if buying:
                    memo[(i, buying)] =  max( dfs(i+1, True), dfs(i+1, False) - prices[i] )
                else:
                    memo[(i, buying)] = max( dfs(i+1, False), dfs(i+2, True) + prices[i] )

                return memo[(i, buying)]
        
        return dfs(0, True)