class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = len(nums) - 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= p - i:
                p = i

        return True if p == 0 else False