class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]
        # mat_t = [[0]*n for _ in range(n)]
        # r = [0]*n
        # c = [0]*n

        for a,b,x,y in queries:
            for i in range(a, x+1):
                for j in range(b, y+1):
                    mat[i][j]+=1

        # print(mat)

        # return [[0]]
        return mat