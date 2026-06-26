class Solution:
    @staticmethod
    def first_end_ge(intervals, bound):
        """First index i with intervals[i][1] >= bound (binary search on end)."""
        l, r = 0, len(intervals)
        while l < r:
            m = (l + r) // 2
            if intervals[m][1] < bound:
                l = m + 1
            else:
                r = m
        return l  # in [0..n]

    @staticmethod
    def first_start_gt(intervals, bound):
        """First index i with intervals[i][0] > bound (binary search on start)."""
        l, r = 0, len(intervals)
        while l < r:
            m = (l + r) // 2
            if intervals[m][0] <= bound:
                l = m + 1
            else:
                r = m
        return l  # in [0..n]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        s, e = newInterval
        # Leftmost candidate to merge: first interval whose end >= s
        l = self.first_end_ge(intervals, s)
        # Right boundary (exclusive): first interval whose start > e
        r = self.first_start_gt(intervals, e)

        # If no overlap (the block to merge is empty), just insert at l
        if l >= r:
            return intervals[:l] + [newInterval] + intervals[l:]

        # Merge intervals[l..r-1] with newInterval
        merged_start = min(s, intervals[l][0])
        merged_end   = max(e, intervals[r-1][1])

        return intervals[:l] + [[merged_start, merged_end]] + intervals[r:]