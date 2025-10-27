class Solution:
    def get_next(self, num):
        result = 0
        while num > 0:
            num,r = divmod(num, 10)
            result += r**2
        return result

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return fast == 1