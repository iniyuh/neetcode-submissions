class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        prev = 0
        for i in range(1, len(intervals)):
            print(intervals[prev], intervals[i])
            if intervals[i][0] <= intervals[prev][1]:
                print("merge")
                intervals[prev][1] = max(intervals[i][1], intervals[prev][1])
            else:
                prev += 1
                intervals[prev], intervals[i] = intervals[i], intervals[prev]
        
        return intervals[:prev+1]

            