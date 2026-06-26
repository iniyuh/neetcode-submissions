class Solution:
    def hammingWeight(self, n: int) -> int:
        extractor = 1
        count = 0

        for i in range(32):
            if n & extractor: count += 1
            extractor = extractor << 1
        
        return count