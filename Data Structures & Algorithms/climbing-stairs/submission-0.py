class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        res1 = self.climbStairs(n - 2)
        res2 = self.climbStairs(n - 1)

        res = 0
        if res1 > 0: res += res1
        if res2 > 0: res += res2

        return res