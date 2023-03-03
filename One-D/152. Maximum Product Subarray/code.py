class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax,currMin = 1,1
        for n in nums:
            temp = currMax * n
            currMax = max(n, temp,currMin*n)
            currMin = min(n, temp,currMin*n)
            res = max(res,currMax)
        return res
        