class Solution:
    def isViable(self, k: int) -> bool:
        if k == 0: return False
        
        sum = 0

        for pile in self.piles:
            sum += math.ceil(pile/k)

        return sum <= self.h
        


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h

        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2

            if self.isViable(m) and not self.isViable(m - 1):
                return m
            elif self.isViable(m):
                r = m - 1
            else: 
                l = m + 1