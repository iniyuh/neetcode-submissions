"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Use a heap which is based on timestamp
Separate starts and ends into distinct entities in the heap
Keep popping from the heap and keep track of how many rooms are used
Keep track of the max number of rooms used
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []
        for interval in intervals:
            heapq.heappush(minHeap, (interval.start, 'START') )
            heapq.heappush(minHeap, (interval.end, 'END') )
        
        maxDays = 0
        currDays = 0
        while minHeap:
            _, type_ = heapq.heappop(minHeap)
            if type_ == 'START': currDays += 1
            else: currDays -= 1

            maxDays = max(maxDays, currDays)
        
        return maxDays

