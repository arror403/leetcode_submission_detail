class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        lr,lc=len(grid),len(grid[0])
        if lr==1 or lc==1: return False
        
        for i in range(lr-1):
            for j in range(lc-1):
                if grid[i][j] == grid[i+1][j] and grid[i][j]!=grid[i][j+1]:
                    continue
                else:
                    return False
        
        return True