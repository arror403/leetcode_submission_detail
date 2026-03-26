class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        return [[sum(sum(x) for x in self.neighbors(mat,k,i+1,j+1))
                for j in range(len(mat[0]))] for i in range(len(mat))]


    def neighbors(self, a, radius, row_number, column_number):
        return [[a[i][j] if i >= 0 and i<len(a) and j>=0 and j<len(a[0]) else 0
                for j in range(column_number-1-radius, column_number+radius)]
                for i in range(row_number-1-radius, row_number+radius)]