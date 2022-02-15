class Solution:
    def fib(self, n: int) -> int:
       
        def fibonacci(x):
            if x <= 1:
                return x
            return fibonacci(x-2) + fibonacci(x-1)
        
        return fibonacci(n)