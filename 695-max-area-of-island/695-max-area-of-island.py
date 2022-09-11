class Solution:
    def dfs(self, i, j, grid, visited):
        if (i,j) in visited or i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == 0: return 0

        visited.add((i,j))
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        ans = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            ans += self.dfs(x, y, grid, visited)
            
        return ans + 1
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i,j) not in visited:
                    maxArea = max(maxArea, self.dfs(i,j,grid,visited))
        return maxArea
        