class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)

        if length == 1:
            return nums[0]
        
        left,right = 0,length-1

        while(left < right):
            if right - left == 1:
                return min(nums[left],nums[right])
            mid = (left + right) / 2
            if nums[left] < nums[mid] and nums[mid] < nums[right]:
                return nums[left]
            elif(nums[left] > nums[mid]):
                right = mid
            else:
                left = mid
        
        return -1