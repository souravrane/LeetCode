class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oldR, oldC = len(mat), len(mat[0])
        if oldR * oldC != r * c : return mat
        
        def nextCell(r,c):
            newC = (c + 1) % oldC
            newR = r
            if c == oldC - 1: newR = (r + 1) % oldR
            return [newR, newC]
            
        curR, curC = 0,0
        newMat = [[0]*c for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                newMat[i][j] = mat[curR][curC]
                curR,curC = nextCell(curR, curC)
        
        return newMat
            