class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        outer_most = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i == 0 and j != 0: outer_most.add(1)
                    if i != 0 and j == 0: outer_most.add(2)
                    if i == 0 and j == 0: outer_most.update([1,2])
                    matrix[0][j] = pow(2,31)
                    matrix[i][0] = pow(2, 31)
        
        #set rows
        for i in range(1, row):
            if matrix[i][0] == pow(2,31):
                matrix[i][0] = 0
                for j in range(1, col):
                    matrix[i][j] = 0
        
        # set cols
        for j in range(1, col):
            if matrix[0][j] == pow(2,31):
                matrix[0][j] = 0
                for i in range(1, row):
                    matrix[i][j] = 0
        
        if 1 in outer_most:
            for j in range(col): matrix[0][j] = 0
        
        if 2 in outer_most:
            for i in range(row): matrix[i][0] = 0