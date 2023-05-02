class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True;
        intervals.sort()
        preEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < preEnd:
                return False;
            preEnd = end
        return True