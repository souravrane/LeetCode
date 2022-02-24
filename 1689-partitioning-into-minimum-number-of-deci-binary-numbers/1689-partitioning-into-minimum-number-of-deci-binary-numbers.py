class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 1
        for num in n:
            max_digit = max(max_digit, int(num))
            
        return max_digit
        
        