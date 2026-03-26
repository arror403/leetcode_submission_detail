class Solution:
    def largestIsland(self, g: List[List[int]]) -> int:
        def paint(i, j, c, g, flip=False):
            if (not flip and (min(i,j)<0 or i>=len(g) or j>=len(g[0]) or g[i][j]==0 or g[i][j]==c)):
                return 0

            g[i][j]=0 if g[i][j]==0 else c

            return 1+paint(i+1, j, c, g)+paint(i-1, j, c, g)+paint(i, j+1, c, g)+paint(i, j-1, c, g)

        res=0
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j]==0:
                    res=max(res, paint(i, j, 2, g, True))
                    paint(i, j, 1, g, True)


        return len(g)*len(g[0]) if res==0 else res