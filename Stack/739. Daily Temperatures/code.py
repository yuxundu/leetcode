class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [ 0 for i in range(n)]
        stack = []
        for i in range(n):
            # print("i:",i,"stack:",stack,"output:",output)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                output[stack[-1]] = i-stack[-1]
                # print("output:",output,"stack[-1]",stack[-1])
                stack.pop()
            stack.append(i)

        return output
        