class Solution:
    def changeRowCol(self, mat, r, c):
        for i in range(len(mat[0])):
            mat[r][i] = pow(2,31) if mat[r][i] != 0 else 0
        
        for i in range(len(mat)):
            mat[i][c] = pow(2,31) if mat[i][c] != 0 else 0


    def setZeroes(self, mat: List[List[int]]) -> None:
        r, c = len(mat), len(mat[0])

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    self.changeRowCol(mat, i, j)
        
        for i in range(r):
            for j in range(c):
                if mat[i][j] == pow(2,31):
                    mat[i][j] = 0            