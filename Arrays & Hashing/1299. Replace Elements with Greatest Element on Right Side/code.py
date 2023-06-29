class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr)-1,-1,-1):
            newRightMax = max(arr[i],rightMax)
            arr[i] = rightMax
            rightMax = newRightMax

        return arr