class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        linearSpread = []
        for i in range(rows):
            for j in range(cols):
                linearSpread.append(grid[i][j])
        
        size = rows*cols
        rotations = k % size
        
        linearSpread = linearSpread[size-rotations:] + linearSpread[:size-rotations]
        
        res = []
        for i in range(0,size,cols):
            res.append(linearSpread[i:i+cols])
        
        return res