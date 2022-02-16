class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1: return False
        
        def recursive_div(n):
            if n == 1: return True
            if n % 4 != 0: return False
            return recursive_div(n/4)
        
        return recursive_div(n)
        