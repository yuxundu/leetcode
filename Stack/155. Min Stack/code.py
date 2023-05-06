class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) > 0:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
        # print("push")
        # print("stack",self.stack)
        # print("minStack",self.minStack)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)
        # print("pop")
        # print("stack",self.stack)
        # print("minStack",self.minStack)
        

    def top(self) -> int:
        # print("top")
        # print("stack",self.stack)
        # print("minStack",self.minStack)
        return self.stack[-1]
        

    def getMin(self) -> int:
        # print("getMin")
        # print("stack",self.stack)
        # print("minStack",self.minStack)
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()