class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        L = len(gas)
        
        def helper(i):
            dist = 0
            g = 0

            while g >= 0:
                if dist == L: return True

                g += gas[i]
                g -= cost[i]

                i = (i + 1) % L
                dist += 1
            
            return False
        
        for start in range(L):
            if helper(start): return start
        
        return -1