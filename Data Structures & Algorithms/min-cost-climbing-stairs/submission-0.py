class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        i = len(cost)
        total = 0
        while i > 1:
            if cost[i-1] < cost[i-2]: 
                total += cost[i-1]
                i -= 1
            else: 
                total += cost[i-2]
                i -= 2
        return total


