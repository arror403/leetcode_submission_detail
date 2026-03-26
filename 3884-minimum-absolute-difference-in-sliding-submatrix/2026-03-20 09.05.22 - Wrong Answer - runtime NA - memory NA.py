class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid)-k+1,len(grid[0])-k+1
        res=[[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                s=set()
                for x in range(k):
                    s.add(grid[i+x][j])
                    s.add(grid[i][j+x])
                    s.add(grid[i+x][j+x])
                    s.add(grid[i][j])
                res[i][j]=min([b-a for a,b in pairwise(sorted(s))], default=0)


        return res