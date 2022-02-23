class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        
        # traverse the diagonals starting from top row
        for i in range(c-2,0,-1):
            row = 0
            col = i
            arr = []
            
            while row < r and col < c:
                arr.append(mat[row][col])
                row += 1
                col += 1
            
            arr.sort()
            
            row = 0
            col = i
            while row < r and col < c:
                mat[row][col] = arr[row]
                row += 1
                col += 1
        
        # traverse the diagonals starting from left column
        for i in range(r-1):
            col = 0
            row = i
            arr = []
            
            while row < r and col < c:
                arr.append(mat[row][col])
                row += 1
                col += 1
                
            arr.sort()
            
            col = 0
            row = i
            
            while row < r and col < c:
                mat[row][col] = arr[col]
                row += 1
                col += 1
            
        return mat
            
            
                