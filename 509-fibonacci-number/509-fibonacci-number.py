class Solution:
    def fib(self, n: int, memoize = {0:0,1:1}) -> int:
        if n in memoize:
            return memoize[n]
        
        memoize[n] = self.fib(n-1,memoize) + self.fib(n-2,memoize)
        return memoize[n]   
    
    