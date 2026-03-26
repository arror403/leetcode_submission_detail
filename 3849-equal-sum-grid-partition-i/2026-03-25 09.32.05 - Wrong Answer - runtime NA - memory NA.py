class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        
        r_sum=list(accumulate([sum(r) for r in grid]))
        for i in range(1,m):
            if r_sum[i]==2*r_sum[i-1]:
                return True

        c_sum=list(accumulate([sum(c) for c in zip(*grid)]))
        for i in range(1,n):
            if c_sum[i]==2*c_sum[i-1]:
                return True


        return False

# [[7,3],
#  [2,5],
#  [5,6]]