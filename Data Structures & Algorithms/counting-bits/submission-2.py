class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range (n + 1):
            counts.append(sum([1 for bit in bin(i)[2:] if bit == '1']))
        return counts
        