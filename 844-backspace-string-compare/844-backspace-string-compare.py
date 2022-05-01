class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #compare from end to start
        
        pS = len(s) - 1
        pT = len(t) - 1
        
        while pS >= 0 or pT >= 0:
            
            skips = 0
            while pS >= 0:
                if s[pS] == "#":
                    skips += 1
                    pS -= 1
                    
                elif skips != 0:
                    pS -= 1
                    skips -= 1
                    
                else: 
                    break
                    
            skips = 0
            while pT >= 0:
                if t[pT] == "#":
                    skips += 1
                    pT -=1 
                    
                elif skips != 0:
                    pT -= 1
                    skips -= 1
                    
                else:  
                    break
                    
            print(pS, ' and ', pT)
            
            if pS >= 0 and pT >= 0 and s[pS] != t[pT]:
                return False
            
            pS -= 1
            pT -= 1
        
        if pS < 0 and pT < 0 and pS == pT: return True
        return False