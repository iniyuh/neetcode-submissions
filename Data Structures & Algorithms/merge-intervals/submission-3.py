class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = []

        logicalInterval = intervals[0]

        for start, end in intervals:
            # overlap
            if start <= logicalInterval[1]:
                logicalInterval[1] = max(end, logicalInterval[1])
            else:
                ret.append(logicalInterval)
                logicalInterval = [start, end]
        ret.append(logicalInterval)

        return ret