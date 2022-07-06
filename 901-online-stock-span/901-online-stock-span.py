class StockSpanner:

    def __init__(self):
        self.priceStack = []
        self.spanStack = []
        self.top = -1
     
    def next(self, price: int) -> int:
        span = 1
        while self.priceStack and price >= self.priceStack[-1]:
            span += self.spanStack[-1]
            self.priceStack.pop()
            self.spanStack.pop()
            self.top -= 1
        
        self.priceStack.append(price)
        self.spanStack.append(span)
        
        self.top += 1
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price) 