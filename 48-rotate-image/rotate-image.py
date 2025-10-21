class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(i, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(row):
            start, end = 0, len(matrix[0]) - 1
            while start < end:
                matrix[i][end], matrix[i][start] = matrix[i][start], matrix[i][end]
                start += 1
                end -= 1