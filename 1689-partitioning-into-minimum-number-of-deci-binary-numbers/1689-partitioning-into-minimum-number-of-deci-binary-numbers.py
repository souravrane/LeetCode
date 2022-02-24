class Solution:
    def minPartitions(self, n: str) -> int:
        '''
        The possible number of deci binary numbers to add 
        upto n will be equal to the highest digit in the number. 
        '''
        '''
        Also I was today years old when i found out applying max on a string
        in python will give you max value from it ! :D
        '''
        return max(n)
        
        