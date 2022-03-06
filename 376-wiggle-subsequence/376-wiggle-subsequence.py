class Solution:
    def wiggleMaxLength(self, num: List[int]) -> int:
        n = len(num)
        count = 1
        
        high = 1
        low = 1
        
        '''
        if the diff is postive then the previous number was supposed to be high , hence high = low + 1
        if the diff is negative then the previous number was supposed to be low , hence low = high + 1

        '''
        for i in range(1,n):
            diff = num[i] - num[i-1]
            if diff > 0:
                high = low + 1
            
            if diff < 0:
                low = high + 1
                
        return max(high,low)
        