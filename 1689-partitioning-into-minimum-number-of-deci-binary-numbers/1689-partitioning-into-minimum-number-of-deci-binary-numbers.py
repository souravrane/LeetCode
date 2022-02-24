class Solution:
    def minPartitions(self, n: str) -> int:
        '''
        The possible number of deci binary numbers to add 
        upto n will be equal to the highest digit in the number. 
        '''
        max_digit = 1
        for num in n:
            max_digit = max(max_digit, int(num))
            
        return max_digit
        
        