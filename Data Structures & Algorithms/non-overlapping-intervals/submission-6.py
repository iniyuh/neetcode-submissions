class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: (interval[0], interval[1]))

        for L, R in intervals:
            print(L, R, R - L)

        ret = 0

        prevL, prevR = intervals[0]

        for L, R in intervals[1:]:
            if L < prevR: 
                ret += 1

                prevR = min(prevR, R)
            else:
                prevL, prevR = L, R
        
        return ret