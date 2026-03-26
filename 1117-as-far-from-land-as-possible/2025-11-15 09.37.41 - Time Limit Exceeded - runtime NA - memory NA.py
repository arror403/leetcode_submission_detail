class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ones=[]
        zeros=[]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ones.append([i,j])
                else:
                    zeros.append([i,j])

        res=-inf
        for x1, y1 in zeros:        
            d=inf
            for x0, y0 in ones:
                d=min(d, abs(x0-x1)+abs(y0-y1))
            if d!=inf:
                res=max(res, d)


        return -1 if res==-inf else res