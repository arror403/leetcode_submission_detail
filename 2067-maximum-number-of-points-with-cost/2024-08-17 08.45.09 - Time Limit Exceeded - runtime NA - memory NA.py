class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n=len(points),len(points[0])

        @lru_cache(maxsize=None)
        def dfs(row, col):
            if row==m: return 0
            max_points=0
            for next_col in range(n):
                cost=abs(next_col-col)
                points_earned=points[row][next_col] + dfs(row+1, next_col) - cost
                max_points=max(max_points, points_earned)
            
            return max_points


        return max(dfs(0, col) for col in range(n))