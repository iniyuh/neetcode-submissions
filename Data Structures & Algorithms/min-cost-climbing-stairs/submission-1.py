class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hm = {}
        def helper(i):
            if i in hm: return hm[i]
            elif i >= len(cost): return 0
            else:
                hm[i] = cost[i] + min(helper(i + 1), helper(i + 2))
        
        for i in range(len(cost) - 1, -1, -1):
            helper(i)
        
        return min(hm[0], hm[1])

        
