class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        def bisect(target, index):
            l, r = 0, len(intervals) - 1

            while l < r:
                m = (l + r) // 2

                if target < intervals[m][index]: r = m - 1
                else: l = m + 1
            
            return r
        
        left_idx = bisect(newInterval[0], 0) + 1
        new_left = []
        for i in range(left_idx):
            if newInterval[0] <= intervals[i][1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
            else: new_left.append(intervals[i])

        right_idx = bisect(newInterval[1], 1) - 1
        new_right = []
        for i in range(len(intervals) - 1, right_idx, -1):
            print(i)
            if newInterval[1] >= intervals[i][0]:
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else: new_right.append(intervals[i])
        new_right.reverse()

        print(left_idx, right_idx)
        print(new_left + [newInterval] + new_right)

        return new_left + [newInterval] + new_right