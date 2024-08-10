class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i in [-1, len(grid)] or j in [-1, len(grid[0])] or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            for direction in directions:
                dfs(i + direction[0], j + direction[1])  
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        return islands