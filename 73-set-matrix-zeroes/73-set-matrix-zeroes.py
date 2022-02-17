class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
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
        
        '''
        # The above solution uses T.C = O(mn) , S.C = O(m+n)
        
        # The below solution uses T.C = O(mn) , S.C = O(1)
        r = len(matrix)
        c = len(matrix[0])

        # mark all the rows with zeroes to None
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    for k in range(c):
                        if k != j and matrix[i][k] != 0: matrix[i][k] = None
        
        # mark all the colum with zeroes to None
        for i in range(c):
            for j in range(r):
                if matrix[j][i] == 0:
                    for k in range(r):
                        if k != j and matrix[k][i] != 0: matrix[k][i] = None
                            
        # mark all Nones to 0s
        for i in range(c):
            for j in range(r):
                if matrix[j][i] == None:
                    matrix[j][i] = 0
        
        

        
                
        