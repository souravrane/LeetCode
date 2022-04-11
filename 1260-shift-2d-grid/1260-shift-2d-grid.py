class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        '''
        Map the [row,col] to a 1D array value
        Calculate the shift for the 1D array
        Map the 1D index back to [newRow, newCol]
        '''
        
        rows = len(grid)
        cols = len(grid[0])
        size = rows*cols

        def posToVal(i,j):
            return i*cols + j
        
        def valToPos(index):
            return [ index // cols, index % cols ]
        
        res = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                newVal = (posToVal(i,j) + k) % size
                newRow, newCol = valToPos(newVal)
                res[newRow][newCol] = grid[i][j]
        
        return res
                
        