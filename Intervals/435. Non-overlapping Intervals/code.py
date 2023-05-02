class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        preEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if preEnd > start:
                ans += 1
                preEnd = min(preEnd,end)
            else:
                preEnd = end
        return ans;