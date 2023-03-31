class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix, postfix = 1,1

        for i in range(0, len(nums)):
            prefix = prefix * (1 if i == 0 else nums[i-1])
            ans[i] = prefix
        for i in range(len(nums)-1,-1,-1):
            postfix = postfix * (1 if i == len(nums)-1 else nums[i+1])
            ans[i] = postfix *  ans[i]
        return ans