class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        
        def recursive_division(x):
            # Base case 1
            if x == 1: return True
            
            # Base case 2
            if int(x) != x: return False
            
            # Recursive case
            return recursive_division(x/3)
        
        return recursive_division(n)
        