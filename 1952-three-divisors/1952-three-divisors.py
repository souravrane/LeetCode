import math
class Solution:
    def isThree(self, n: int) -> bool:
        '''
        The number should be a prime number square.
        Only then it can have 3 divisors.
        
        1 prime prime^2
        
        '''
        if n <= 3: return False
        
        if math.floor(math.sqrt(n)) != math.ceil(math.sqrt(n)):
            return False
        
        for i in range(2,int(math.sqrt(n))):
            if n % i == 0: return False
        
        return True