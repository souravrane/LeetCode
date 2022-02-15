class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = 1
        if x < 0 and n % 2 == 1: flag = -1
            
        power = abs(n)
        a = abs(x)
        res = 1
        while power > 0:
            if power % 2 == 1:
                res *= a
            
            a = a*a
            power = power // 2
        
        if n < 0: return flag*(1/res)
        return flag*res
            
        
            
            
        
        
        