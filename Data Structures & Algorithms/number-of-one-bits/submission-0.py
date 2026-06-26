class Solution:
    def hammingWeight(self, n: int) -> int:
        def count(n):
            if n == 0: return 0
            elif n & 1: return 1 + count(n >> 1)
            else: return count(n >> 1)
        
        return count(n)