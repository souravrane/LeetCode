class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_min = []
        self.topx = -1
    

    def push(self, x: int) -> None:
        self.topx += 1
        if self.topx == 0:
            self.stack.append(x)
            self.prefix_min.append(x)
            return
        
        min_element = min(self.prefix_min[self.topx-1],x)
        self.stack.append(x)
        self.prefix_min.append(min_element)
        

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_min.pop()
        self.topx -= 1
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()