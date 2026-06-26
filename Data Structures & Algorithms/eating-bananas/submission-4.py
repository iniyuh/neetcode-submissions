"""
For a given k, calculating t is O(n) where n is the number of piles,
    so calculating validity of k is O(n) time and O(1) space
We want to find k such that k is valid and k - 1 is invalid (aka min valid k)
Call max(piles) M
Method 1: 
    for each pile find and store the minimum k for it and store
        could iterate up from 1 to M so O(M)
        OR 
        could binary search 1 to M range, so O(logM)
    take the max of these k's for the answer
    Overall: time is O(n * logM) space is O(n)
Method 2: 
    Immediate bin search on same range (1 to M) and verify all piles O(n)
    So O(logM * n), same thing different implementation
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) + 1

        while l < r:
            k = (l + r) // 2

            if self.feasible(piles, h, k):
                if not self.feasible(piles, h, k - 1): return k
                else:
                    r = k
            else:
                l = k + 1
    
    def feasible(self, piles, h, k):
        if k == 0: return False

        t = 0
        for pile in piles:
            t += math.ceil(pile / k) 
            
            if t > h: return False
        return True

