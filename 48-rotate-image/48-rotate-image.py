class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        
        # transpose
        for i in range(r):
            for j in range(i,c):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # row reversal
        for i in range(r):
            s = 0
            e = c-1
            while s < e:
                matrix[i][s], matrix[i][e] = matrix[i][e], matrix[i][s]
                s += 1
                e -= 1
        
        
        