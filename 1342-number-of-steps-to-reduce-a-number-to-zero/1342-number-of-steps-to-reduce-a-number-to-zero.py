class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1
            if num % 2:
                num = num - 1
            else:
                num = num >> 1
        return count
        