class Solution:
    def wiggleMaxLength(self, num: List[int]) -> int:
        n = len(num)
        count = 1
        
        high = 1
        low = 1
        
        for i in range(1,n):
            diff = num[i] - num[i-1]
            if diff > 0:
                high = low + 1
            
            if diff < 0:
                low = high + 1
                
        return max(high,low)
        