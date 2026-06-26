class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ret = max(piles)

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if h < hours:
                l = k + 1
            else:
                ret = min(k, ret)
                r = k - 1
        
        return ret
            
        
        return ret

