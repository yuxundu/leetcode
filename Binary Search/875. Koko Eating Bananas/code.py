class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = max(piles)
        while l <= r:
            mid = l + (r-l)//2
            countH = 0
            for num in piles:
                countH += -(num//-mid)
            print("mid:",mid,"countH:",countH)
            if countH > h:
                l = mid + 1
            else:
                r = mid - 1
                res = min(res,mid)  
        return res