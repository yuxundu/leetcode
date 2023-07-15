class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counters = {}
        for w,h in rectangles:
            counters[w/h] = 1 + counters.get(w/h,0)
        res = 0 
        for count in counters.values():
            res += (count*(count-1))//2
        return res
