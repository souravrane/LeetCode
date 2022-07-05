from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def isValid(i,j):
            if (i < 0 or i >= rows) or (j < 0 or j >= cols): return False
            if grid[i][j] == 1: return True
            if grid[i][j] in [0,2]: return False
        
        currentState = deque()
        nextState = deque()
        oranges = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: oranges += 1
                if grid[i][j] == 2: currentState.append((i,j))
          
        if oranges == 0: return 0
        
        days = -1
        while currentState:
            days += 1
            s = len(currentState)

            for i in range(s):
                i,j = currentState.popleft()

                if isValid(i+1,j):
                    currentState.append((i+1,j))
                    grid[i+1][j] = 2
                    oranges -= 1

                if isValid(i-1,j):
                    currentState.append((i-1,j))
                    grid[i-1][j] = 2
                    oranges -= 1

                if isValid(i,j+1):
                    currentState.append((i,j+1))
                    grid[i][j+1] = 2
                    oranges -= 1

                if isValid(i,j-1):
                    currentState.append((i,j-1))
                    grid[i][j-1] = 2
                    oranges -= 1


        if oranges == 0:
            return days
        
        return -1