class Solution:
    def climbStairs(self, n: int) -> int:
        hm = {}
        def rec(n):
            if n <= 2: return n
            elif n in hm: return hm[n]
            else:
                hm[n] = rec(n - 2) + rec(n - 1)
                return hm[n]
        
        return rec(n)
        