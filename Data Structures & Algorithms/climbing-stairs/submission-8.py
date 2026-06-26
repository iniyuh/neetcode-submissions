class Solution:
    def climbStairs(self, n: int, i: int = 0) -> int:
        if n - i <= 2: return n - i
        else:
            return self.climbStairs(n, i+1) + self.climbStairs(n, i+2)
        