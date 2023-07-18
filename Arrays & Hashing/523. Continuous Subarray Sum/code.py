class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = {0:-1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainderMap:
                remainderMap[r] = i
            elif i - remainderMap[r] > 1:
                return True    

        return False