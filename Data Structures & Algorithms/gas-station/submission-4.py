class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0

        currMax, currIdx = 0, None
        globalMax, globalIdx = -1, None
        
        for i in range(2 * len(gas)):
            i = i % len(gas)

            total += gas[i] - cost[i]
            currMax += gas[i] - cost[i]

            if currMax < 0: 
                currIdx = None
                currMax = 0
            elif currIdx is None:
                currIdx = i
            
            if currMax > globalMax:
                globalIdx = currIdx
                globalMax = currMax
        
        if total < 0: return -1
        else: return globalIdx