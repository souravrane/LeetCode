import math

class Solution:
    def reverse(self, x: int) -> int:
        MAX = int(2**31) - 1
        MIN = -int(2**31)
        
        reverse = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x / 10)
            
            if (reverse > MAX // 10) or (reverse == MAX // 10 and digit > MAX % 10): return 0
            if (reverse < MIN // 10) or (reverse == MIN // 10 and digit < MIN % 10): return 0
            
            reverse = reverse*10 + digit
        
        return reverse