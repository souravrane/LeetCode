class Solution:
    def power(self,a,b,m):
        if b == 0: return 1
        
        hp = self.power(a,b//2,m)
        
        if b % 2 == 0:
            return (hp * hp) % m
        else:
            return (hp * hp * a) % m
        
    def superPow(self, a: int, b: List[int]) -> int:
        '''
        ETF = Euler Totient Function
        ETF(x) = count of all numbers that are copirme with x and are less than x
        
        Euler Theorem 
        a^b % m = a^(b % ETF(m)) % m
        
        ETF(1337) = 1337 * (1-1/7) * (1-1/191)
                  = 1140
        
        '''
        
        '''
        We can write (2456) % m as (2000 + 400 + 50 + 6) % m
        So we build the number from right to left
        '''
        newB = 0
        for num in b:
            newB = (newB * 10 + num) % 1140
        
        return self.power(a,newB,1337)