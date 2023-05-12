class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                maxArea = max(maxArea, (i - stack[-1][0]) * stack[-1][1])
                start = stack[-1][0]
                stack.pop()
                
            stack.append((start,heights[i]))
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights)-i))
        return maxArea
        