class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        p=[[0]*n for _ in range(m)]
        f=1

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='X':
                    p[i][j]=1
                    f=0
                if grid[i][j]=='Y':
                    p[i][j]=-1
                    f=0

        if f: return 0

        pr=[list(accumulate(r)) for r in p]
        pc=[list(accumulate(c)) for c in zip(*pr)]


        return len([v for v in chain.from_iterable(pc) if v==0])

# [["X","Y","."],
#  [".",".","."],
#  ["Y",".","X"],
#  ["X","Y","."]]

# [(1, 0, 0), 
#  (1, 0, 0), 
#  (0, -1, 0), 
#  (1, -1, 0)]