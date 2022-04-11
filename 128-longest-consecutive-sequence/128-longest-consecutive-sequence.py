class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longestSeq = 0
        
        d = defaultdict(bool)
        
        for i in nums: d[i] = True
        
        for i in nums:
            
            if d[i] == True:
                
                d[i] = False
                
                # check left range
                left = 0
                x = i-1
                while d[x] == True:
                    d[x] = False
                    left += 1
                    x -= 1
                    
                
                # check right range
                right = 0
                x = i+1
                while d[x] == True:
                    d[x] = False
                    right += 1
                    x += 1
                
                longestSeq = max(longestSeq, left + right + 1)
        
        return longestSeq
                    
            
