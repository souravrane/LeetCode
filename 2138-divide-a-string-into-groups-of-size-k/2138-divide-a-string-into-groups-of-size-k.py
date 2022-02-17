class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        pending_x = len(s) % k
        res = []
        for i in range(0,len(s),k):
            if i+k <= len(s):    
                res.append(s[i:i+k])
        
        if pending_x > 0:
            res.append(s[-pending_x:] + fill*(k-pending_x))
        
        return res
    
        