class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x = 1
        top,left = 0,0
        bottom,right = n-1, n-1
        
        res = [[0]*n for i in range(n)]
        
        while top <= bottom and left <= right:
            
            for i in range(left,right+1):
                res[top][i] = x
                x += 1
            
            top += 1
            
            for i in range(top,bottom+1):
                res[i][right] = x
                x += 1
            
            right -= 1
            
            for i in range(right,left-1,-1):
                res[bottom][i] = x
                x += 1
            
            bottom -= 1
            
            for i in range(bottom,top-1,-1):
                res[i][left] = x
                x += 1
            
            left += 1
            
        return res