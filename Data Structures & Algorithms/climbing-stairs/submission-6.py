class Solution:
    def climbStairs(self, n: int) -> int:
        hm = {}

        def helper(i):
            if i == n - 1: return 1
            elif i == n - 2: return 2
            elif i in hm: return hm[i]
            else:
                hm[i] = helper(i + 1) + helper(i + 2)
                return hm[i]
        
        return helper(0)


