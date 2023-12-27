class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        tot=0
     
        for row in grid:
        
            for j in range(n):
                col=[grid[i][j] for i in range(n)]

                # print(row,col)
                if row==col:
                    tot+=1
                    # print(row,col)

        return tot
