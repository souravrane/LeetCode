class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if i not in row: row.add(i)
                    if j not in col: col.add(j)

        for x in row:
            for j in range(c):
                matrix[x][j] = 0
        
        for x in col:
            for j in range(r):
                matrix[j][x] = 0
        
                
        