class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        
        nS, nE = newInterval

        if nE < intervals[0][0]: return [newInterval] + intervals
        elif intervals[-1][1] < nS: return intervals + [newInterval]

        left, right = None, None

        prevEnd = None

        for i, (s, e) in enumerate(intervals):
            # Overlap
            if (
                s <= nS <= e or 
                s <= nE <= e or
                nS <= s <= nE or
                nS <= e <= nE
            ):
                print("HIT", s, e)
                if left is None: left = i
                right = i
            elif prevEnd is not None and prevEnd < nS <= nE < s:
                intervals.insert(i, newInterval)
                return intervals
            
            prevEnd = e
        

        updatedStart = min(nS, intervals[left][0])
        updatedEnd = max(nE, intervals[right][1])

        return intervals[:left] + [[updatedStart, updatedEnd]] + intervals[right+1:]
