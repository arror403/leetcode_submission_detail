class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = set()
        n, m = len(matrix), len(matrix[0])
        pacific = [[0]*n for _ in range(m)]
        atlantic = [[0]*n for _ in range(m)]

        for i in range(n):
            self.dfs(matrix, pacific, -inf, i, 0)
            self.dfs(matrix, atlantic, -inf, i, m-1)

        for i in range(m):
            self.dfs(matrix, pacific, -inf, 0, i)
            self.dfs(matrix, atlantic, -inf, n-1, i)

        for i in range(n):
            for j in range(m):
                if (pacific[i][j] and atlantic[i][j]):
                    res.add((i, j))


        return [list(p) for p in res]
    
    
    
    def dfs(self, matrix, visited, height, x, y):
        n, m = len(matrix), len(matrix[0])
        if (x<0 or x>=n or y<0 or y>=m or visited[x][y] or matrix[x][y] < height):
            return
        visited[x][y] = True
        for d in self.directions:
            self.dfs(matrix, visited, matrix[x][y], x+d[0], y+d[1])