class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        O(M+N)
        As they are row and column wise sorted we can start traversing from top right corner
        if corner is smaller than the element then we move downwards to the next row
        if corner is greater than the element then we move leftwords to the previous column
        This way we will reach our element and return true or exit the matrix bounds and return false
        
        '''
        rows = len(matrix)
        columns = len(matrix[0])
        
        i,j = 0,columns-1
        
        while i < rows and j >= 0:
            
            if matrix[i][j] == target:
                return True
            
            if target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        
        return False
        
        