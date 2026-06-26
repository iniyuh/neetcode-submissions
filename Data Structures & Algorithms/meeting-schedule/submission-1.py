"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for interval1 in intervals:
            for interval2 in intervals:
                if interval1 == interval2: continue
                if interval1.end <= interval2.start or interval1.start >= interval2.end: continue
                return False
        
        return True