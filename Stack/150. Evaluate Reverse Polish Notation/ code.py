class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(int(a)+int(b))
            elif tokens[i] == "-":
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(int(a)-int(b))
            elif tokens[i] == "*":
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(int(a)*int(b))
            elif tokens[i] == "/":
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                stack.append(int(int(a)/int(b)))
            else:
                stack.append(tokens[i])
        return int(stack[0])