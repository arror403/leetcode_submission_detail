class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        row_len=max([len(i) for i in nums])

        for i in nums:
            while len(i)<row_len:
                i.append(0)
            # for j in range(row_len):
        return self.convert_util(nums)


    def convert_util(self, matrix):
        num_rows, num_cols = len(matrix), len(matrix[0])
        result = []

        for d in range(num_rows + num_cols - 1):
            if d % 2 == 0:
                row = min(d, num_rows - 1)
                col = max(0, d - num_rows + 1)
            else:
                row = max(0, d - num_cols + 1)
                col = min(d, num_cols - 1)
                
            diagonal = []

            while row >= 0 and col >= 0 and row < num_rows and col < num_cols:
                tmp=matrix[row][col]
                if tmp!=0: diagonal.append(tmp)

                if d % 2 == 0:
                    row -= 1
                    col += 1
                else:
                    row += 1
                    col -= 1

            # Reverse the order of elements in odd diagonals
            if d % 2 != 0:
                diagonal = list(reversed(diagonal))

            result.extend(diagonal)

        return result