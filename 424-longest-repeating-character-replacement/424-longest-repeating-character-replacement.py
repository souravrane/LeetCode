class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestSub = 0
        
        for i in range(26):
            searchChar = chr(ord('A') + i)
            start = -1
            end = -1
            missMatch = 0
            
            while end < len(s) - 1:
                if s[end + 1] != searchChar:


                    if missMatch < k:
                        missMatch += 1


                    else:
                        start += 1
                        while s[start] == searchChar :
                            start += 1
                    
                end += 1
                longestSub = max(longestSub, end - start)  
                    
        
        return longestSub
                    
                    
                        