class Solution:
    def dfs(self, grid, x, y, visited):
        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == "0" or visited[x][y]: return
        visited[x][y] = True
        self.dfs(grid, x+1, y, visited)
        self.dfs(grid, x-1, y, visited)
        self.dfs(grid, x, y+1, visited)
        self.dfs(grid, x, y-1, visited)


        
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        islands = 0
        visited = [[False] * c for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] != "0" and visited[i][j] == False:
                    self.dfs(grid, i, j, visited)
                    islands += 1
        
            
        return islands
        