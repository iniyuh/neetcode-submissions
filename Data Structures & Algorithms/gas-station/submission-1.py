class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [gas[i] - cost[i] for i in range(len(gas))]
        curr = 0
        total = 0
        anchor = 0

        for i, diff in enumerate(diffs):
            curr += diff
            total += diff
            if curr < 0: 
                curr = 0
                anchor = i + 1
        
        return anchor if total >= 0 else -1

        
