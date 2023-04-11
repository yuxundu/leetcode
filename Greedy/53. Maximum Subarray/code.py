class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        total = 0
        for n in nums:
            total = total + n
            ans = max(total,ans)
            if total < 0:
                total = 0
        return ans
            