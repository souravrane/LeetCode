class Solution:
    def minFlips(self, s: str) -> int:
        '''
        Flip operation : 
            We can get the number of type 2 operations by comparing the original string with 2 different strings 
            1. 0101...
            2. 1010...
        
        Remove operation : 
            Now lets see how type 1 operation can be put to use.
            We can remove the first element and place it at the end and then perform the FLip operation as stated above again. 
            We keep doing this till we reach the end of the original string by doing the remove operation and keep updating the minFlips.
            
        We can achieve this optimally by using sliding window technique
        our window size is original strings length, every tuime we move the window we check if the removed elements was alternating or not. If it wasnt 
        we remove it from our initial count.
        We perform the same check on the element that we added in the end, if that was not alternating we increment our flip count.
        
        We perform this and keep updating our min flips

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
        
        toggle = 1-int(alternating0[-1])
        for i in range(windowSize,n):
            alternating0 += str(toggle)
            toggle = 1 - toggle
            
        toggle = 1-int(alternating1[-1])
        for i in range(n):
            alternating1 += str(toggle)
            toggle = 1 - toggle
            
        
        minFlips = min(currFlipsForAlt0, currFlipsForAlt1)
        
        for i in range(1,windowSize):
            # for 0101 alternating
            if newS[i-1] != alternating0[i-1]: currFlipsForAlt0 -= 1
            if newS[i + windowSize-1] != alternating0[i + windowSize - 1]: currFlipsForAlt0 += 1
            
            # for 1010 alternating
            if newS[i-1] != alternating1[i-1]: currFlipsForAlt1 -= 1
            if newS[i + windowSize-1] != alternating1[i + windowSize - 1]: currFlipsForAlt1 += 1
        
            minFlips = min(currFlipsForAlt0, currFlipsForAlt1, minFlips)
        
        return minFlips
        
        