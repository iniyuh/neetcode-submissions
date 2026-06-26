class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ret = 0
        prev = intervals[0]
        print(intervals)

        for curr in intervals[1:]:
            if prev[0] == curr[0] or curr[0] < prev[1]:
                if curr[1] < prev[1]: prev = curr
                ret += 1
            # elif curr[0] < prev[1]:
            #     ret += 1
            else:
                prev = curr
        
        return ret