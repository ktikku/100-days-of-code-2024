class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m,n = len(grid),len(grid[0])
        M,N = 3*m,3*n
        grid1 = [[0]*N for _ in range(M)]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/':
                    i1,j1 = 3*i,3*j
                    grid1[i1][j1+2] = 1
                    grid1[i1+1][j1+1] = 1
                    grid1[i1+2][j1] = 1
                elif grid[i][j] == '\\':
                    i1,j1 = 3*i,3*j
                    grid1[i1][j1] = 1
                    grid1[i1+1][j1+1] = 1
                    grid1[i1+2][j1+2] = 1

        def dfs(r,c):
            if r in [-1,M] or c in [-1,N] or grid1[r][c] == 1: return
            grid1[r][c] = 1
            print('Covering in iteration:', r,c)
            for dx,dy in directions: 
                dfs(r+dx,c+dy)

        for i in range(M):
            for j in range(N):
                if grid1[i][j] == 0:
                    print('starting from:', i, j)
                    dfs(i,j)
                    res+=1
                    print('No of regions:', res)
        return res