class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robOne(nums[1:]),self.robOne(nums[:-1]))

    def robOne(self,nums):
        rob1,rob2 = 0,0
        for n in nums:
            rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = rob
        return rob2

        