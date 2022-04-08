class Solution:
    def fibonacci(self,n,s):
        if n in s:
            return s[n]
        
        s[n] = self.fibonacci(n-1,s) + self.fibonacci(n-2,s)
        return s[n]
    
    def fib(self, n: int) -> int:
        return self.fibonacci(n,{0:0,1:1})    
    
    