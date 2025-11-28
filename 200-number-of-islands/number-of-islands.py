class Solution:
    def dfs(self, i, j, visited, grid):
        if i < 0 or i >= len(visited): return
        if j < 0 or j >= len(visited[0]): return
        if grid[i][j] == "0": return
        if visited[i][j] == 1: return 

        visited[i][j] = 1

        self.dfs(i+1,j,visited,grid)
        self.dfs(i-1,j,visited,grid)
        self.dfs(i,j-1,visited,grid)
        self.dfs(i,j+1,visited,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    self.dfs(i,j,visited, grid)
                    result += 1

        return result 