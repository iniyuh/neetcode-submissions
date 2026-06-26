class Solution:
    def reverseBits(self, n: int) -> int:
        placeOut = 0b10000000000000000000000000000000
        placeIn = 0b1

        ret = 0

        for _ in range(32):
            if placeIn & n > 0: ret += placeOut
            placeOut = placeOut >> 1
            placeIn = placeIn << 1
        
        return ret