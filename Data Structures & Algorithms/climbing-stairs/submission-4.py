class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        i = 2
        rec = [1, 2]
        
        while i < n:
            temp = rec[1]
            rec[1] = rec[0] + rec[1]
            rec[0] = temp
            i += 1

        return rec[1]
        