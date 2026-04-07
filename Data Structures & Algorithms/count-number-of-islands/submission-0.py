class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        q = []
        ans = 0
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == '1'):
                    ans += 1
                    q = [(i,j)]
                    grid[i][j] = '0'

                    while q:
                        r,c = q.pop(0)
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr,nc = r+dr, c + dc
                            if (nr > -1 and nc > -1 and nr < n and nc < m and grid[nr][nc] == '1'):
                                q.append((nr,nc))
                                grid[nr][nc] = '0'
        return ans