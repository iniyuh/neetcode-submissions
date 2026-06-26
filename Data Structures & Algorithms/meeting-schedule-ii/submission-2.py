"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start with 1 day
        # keep adding meetings while not overlapping with any 1 of our days
        # if meeting is overlapping with ALL days, create new day

        # need:
        # function to check if meeting overlaps with a day (interval and set of intervals)

        if not intervals: return 0

        def binarySearch(day, meeting):
            l, r = 0, len(day)  # half-open [l, r)
            while l < r:
                m = (l + r) // 2
                if day[m].start < meeting.start:
                    l = m + 1
                else:
                    r = m
            return l


        def helper(day, meeting):
            idx = binarySearch(day, meeting)
            print("Idx", idx)

            if (
                (idx - 1 >= 0 and meeting.start < day[idx - 1].end) or 
                (idx + 1 < len(day) and meeting.start == day[idx + 1].start) or
                (idx + 1 < len(day) and day[idx + 1].start < meeting.end)
            ): return None
            else: return idx
        
        days = [[]]

        for meeting in intervals:
            scheduled = False

            for i in range(len(days)):
                val = helper(days[i], meeting)
                if val is not None: 
                    print("Meeting", meeting.start, meeting.end, "goes into day", i)
                    days[i].insert(val, meeting)
                    scheduled = True
                    break
            
            if not scheduled: days.append([meeting])

        return len(days)