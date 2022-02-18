class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        columns = len(mat[0])
        
        # prefix matrix
        pf = [[0 for i in range(columns)] for j in range(rows)]
        
        for i in range(rows):
            pf[i][0] = mat[i][0]
            for j in range(1,columns):
                pf[i][j] = pf[i][j-1] + mat[i][j]

        
        res = [[0 for i in range(columns)] for j in range(rows)]
        
        
        # Write down test cases and come up with logic.
        # traversal is the key here
        for i in range(rows):
            for j in range(columns):
                
                left_col = max(0,j-k)
                right_col = min(columns-1,j+k)
                
                upper_row = max(0,i-k)
                lower_row = min(rows-1,i+k)
                
                s = 0
                for x in range(upper_row,lower_row+1):
                    if left_col == 0:
                        s += pf[x][right_col]
                    else:
                        s += pf[x][right_col] - pf[x][left_col-1]
                
                res[i][j] = s
        
        return res
                
                
'''
k = 1
[1,2,3] [1 3  6 ]
[4,5,6] [4 9  15]
[7,8,9] [7 15 24]

[12,21,16]
[27,45,33]
[24,39,28]

'''