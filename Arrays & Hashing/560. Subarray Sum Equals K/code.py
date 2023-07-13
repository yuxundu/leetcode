class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = {0:1}
        sum, res = 0, 0
        for num in nums:
            sum += num
            res += prefixSumCount.get(sum-k,0)
            prefixSumCount[sum] = 1+prefixSumCount.get(sum,0)
            
        return res
        