class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1

        while i < j:
            count = numbers[i] + numbers[j]
            if count == target:
                return [i+1,j+1]
            if count > target:
                j -= 1
            else:
                i += 1
        return []