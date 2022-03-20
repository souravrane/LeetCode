class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        columns = len(matrix[0])
        
        # row wise prefix
        for i in range(rows):
            for j in range(1,columns):
                matrix[i][j] += matrix[i][j-1]
        
        #column wise prefix
        for i in range(columns):
            for j in range(1,rows):
                matrix[j][i] += matrix[j-1][i]
                
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        
        ans += self.matrix[row2][col2]
        
        if col1 > 0:
            ans -= self.matrix[row2][col1-1]
       
        if row1 > 0:
            ans -= self.matrix[row1-1][col2]
            
        if row1 > 0 and col1 > 0:
            ans += self.matrix[row1-1][col1-1]
      
        return ans
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)







