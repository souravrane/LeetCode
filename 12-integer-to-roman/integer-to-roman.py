class Solution:
    def intToRoman(self, num: int) -> str:
        table = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}
        ans = list()
        while num > 0:
            divisor = self.getDivisor(table, num)
            quo = num // divisor
            ans.append(table[divisor]*quo)
            num = num % divisor
        return ''.join(ans)
    
    def getDivisor(self, table, num):
        maxDiv = 1
        for k in table:
            if k <= num:
                maxDiv = max(maxDiv, k)
        return maxDiv

        