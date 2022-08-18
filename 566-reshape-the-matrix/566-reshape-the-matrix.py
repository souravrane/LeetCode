class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oldR, oldC = len(mat), len(mat[0])
        if oldR * oldC != r * c : return mat

        curR, curC = 0,0
        newMat = [[0]*c for i in range(r)]
        cell = 0
        
        for i in range(r):
            for j in range(c):
                cell += 1
                newMat[i][j] = mat[curR][curC]
                curR, curC = cell // oldC , cell % oldC
        
        return newMat
            