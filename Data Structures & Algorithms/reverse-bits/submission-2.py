class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            bit = (0b1 << i) & n
            if bit: ret += 1 << (31-i)
        return ret
