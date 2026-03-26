class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return word in self.find_sequences(board,len(word))


    def is_valid_move(self, matrix, visited, row, col, length):
        rows=len(matrix)
        cols=len(matrix[0])

        if row<0 or row>=rows or col<0 or col>=cols or visited[row][col]:
            return False

        return True


    def dfs(self, matrix, visited, row, col, length, path, sequences):
        if length==0:
            sequences.append(path)
            return

        visited[row][col]=True

        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        for dr,dc in directions:
            new_row=row+dr
            new_col=col+dc

            if self.is_valid_move(matrix, visited, new_row, new_col, length-1):
                self.dfs(matrix, visited, new_row, new_col, length-1, path+matrix[new_row][new_col], sequences)

        visited[row][col]=False


    def find_sequences(self, matrix, length):
        sequences=[]
        rows=len(matrix)
        cols=len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                visited=[[False]*cols for _ in range(rows)]
                self.dfs(matrix, visited, i, j, length - 1, matrix[i][j], sequences)

        return sequences