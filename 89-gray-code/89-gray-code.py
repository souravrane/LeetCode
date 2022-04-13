class Solution:
    def grayCode(self, n: int, res=[0,1]) -> List[int]:
        if n == 1: return res
        
        gc = self.grayCode(n-1,res)
        
        temp = []
        for x in gc[::-1]:
            temp.append(1<<(n-1) | x)
        gc = gc + temp
        
        return gc