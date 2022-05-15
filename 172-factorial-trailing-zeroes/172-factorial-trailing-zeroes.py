class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        i = 1
        while n // (5**i) > 0:
            count += n // (5**i)
            i += 1
        
        return count