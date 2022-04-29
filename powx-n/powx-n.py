class Solution:
    def power(self, x, n):
        if n == 0: return 1
        hp = self.power(x, n // 2)
        if n % 2 == 0:
            return hp * hp
        else:
            return hp * hp * x
        
    def myPow(self, x: float, n: int) -> float:
        ans = self.power(x, abs(n))
        if n < 0:
            return 1 / ans
        
        return ans