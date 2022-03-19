class Solution:
    def minFlips(self, s: str) -> int:
        '''
        
        ''' 
        n = len(s)
        windowSize = n
        
        toggle = 0
        alternating0 = ""
        for i in range(n):
            alternating0 += str(toggle)
            toggle = 1 - toggle
        
        toggle = 1
        alternating1 = ""
        for i in range(n):
            alternating1 += str(toggle)
            toggle = 1 - toggle
            
        currFlipsForAlt0 = 0
        currFlipsForAlt1 = 0
        
        for i in range(n):
            if s[i] != alternating1[i]: currFlipsForAlt1 += 1
            if s[i] != alternating0[i]: currFlipsForAlt0 += 1
                
        if currFlipsForAlt0 == 0 or currFlipsForAlt1 == 0:
            return 0
        
        '''
        This part takes care of Type 1 operation, that is adding first character
        to the end of the string.
        
        '''
        newS = s + s
        n = len(newS)
        
        toggle = 0
        newAlternating0 = ""
        for i in range(n):
            newAlternating0 += str(toggle)
            toggle = 1 - toggle
            
        toggle = 1
        newAlternating1 = ""
        for i in range(n):
            newAlternating1 += str(toggle)
            toggle = 1 - toggle
            
        
        minFlips = min(currFlipsForAlt0, currFlipsForAlt1)
        
        for i in range(1,windowSize):
            # for 0101 alternating
            if newS[i-1] != newAlternating0[i-1]: currFlipsForAlt0 -= 1
            if newS[i + windowSize-1] != newAlternating0[i + windowSize - 1]: currFlipsForAlt0 += 1
            
            # for 1010 alternating
            if newS[i-1] != newAlternating1[i-1]: currFlipsForAlt1 -= 1
            if newS[i + windowSize-1] != newAlternating1[i + windowSize - 1]: currFlipsForAlt1 += 1
        
            minFlips = min(currFlipsForAlt0, currFlipsForAlt1, minFlips)
        
        return minFlips
        
        