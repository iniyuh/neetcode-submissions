class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = {}
        
        def dfs(i, currentWeight):
            if i == len(profit): return 0
            if (i, currentWeight) in memo: return memo[(i, currentWeight)]

            memo[(i, currentWeight)] = max(
                dfs(i+1, currentWeight),
                profit[i] + dfs(i+1, currentWeight + weight[i]) if currentWeight + weight[i] <= capacity else 0
            )

            return memo[(i, currentWeight)]
        
        return dfs(0, 0)