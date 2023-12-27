from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        cg=[]
        for j in range(n):
            col=[grid[i][j] for i in range(n)]
            cg.append(tuple(col))

        hash_map = defaultdict(int)
        for row in grid:
            hash_map[tuple(row)] += 1

        tot=0
        for col in cg:
            if col in hash_map:
                tot += hash_map[col]

        return tot


        