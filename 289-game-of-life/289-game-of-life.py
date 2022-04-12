class Solution:    
    '''
    old  | new | value
     0   |  0  |   0
     1   |  0  |   1
     0   |  1  |   2
     1   |  1  |   3

    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
                
        rows = len(board)
        cols = len(board[0])
        
        def countNeighbors(i,j):
            count = 0
            top = max(0,i-1)
            bottom = min(rows-1, i+1)
            left = max(0,j-1)
            right = min(cols-1, j+1)
            
            for r in range(top,bottom+1):
                for c in range(left,right+1):
                    if r == i and c == j: continue
                    if board[r][c] in [1,3]: count += 1
            
            return count
            
        

        
        for i in range(rows):
            for j in range(cols):
                cell = board[i][j]
                nei = countNeighbors(i,j)

                if cell == 1:
                    if nei in [2,3]:
                        board[i][j] = 3
                else:
                    if nei == 3:
                        board[i][j] = 2
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1: board[i][j] = 0
                elif board[i][j] in [2,3]: board[i][j] = 1
        
                    
            