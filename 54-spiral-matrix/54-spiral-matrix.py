class Solution:
    def spiral(self,matrix, top, bottom, left, right, res):
        if top > bottom or left > right: return

        for i in range(left,right+1):
            res.append(matrix[top][i])
            
        for i in range(top+1,bottom+1):
            res.append(matrix[i][right])
        
        if top + 1 <= bottom:
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom][i])
        
        if left + 1 <= right:
            for i in range(bottom-1,top,-1):
                res.append(matrix[i][left])

        
        self.spiral(matrix, top+1, bottom-1, left+1, right-1, res)
        
        

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        self.spiral(matrix,0,len(matrix)-1,0,len(matrix[0])-1,res)
        return res