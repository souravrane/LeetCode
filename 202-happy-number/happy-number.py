class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1:
            num = str(n)
            ans = 0
            for x in num: ans += int(x)**2
            if  ans in seen: return False
            seen.add(ans)
            n = ans
        return True
        