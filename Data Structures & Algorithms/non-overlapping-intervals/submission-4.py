class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        intervals.sort()

        prevEnd = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if start < prevEnd:
                count += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        
        return count

