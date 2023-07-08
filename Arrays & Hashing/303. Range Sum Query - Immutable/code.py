class NumArray:

    def __init__(self, nums: List[int]):
        self.previousSum = [0] * len(nums)
        self.previousSum[0] = nums[0]
        for i in range(1,len(nums)):
            self.previousSum[i] = self.previousSum[i-1]  + nums[i]

        

    def sumRange(self, left: int, right: int) -> int:
        leftSum = 0 if left == 0 else self.previousSum[left-1]
        return self.previousSum[right] - leftSum