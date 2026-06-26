class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(n):
            if n == 0: return 0
            elif n & 1: return 1 + count(n >> 1)
            else: return count(n >> 1)

        arr = []
        for i in range(0, n + 1):
            arr.append(count(i))
        
        return arr