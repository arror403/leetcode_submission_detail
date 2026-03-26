class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='.':
                    for c in "123456789": # Trial, try 1 through 9
                        if (self.isValid(board, i, j, c)):
                            board[i][j] = c # Put c for this cell
                            if self.solveSudoku(board):
                                return True # If it's the solution return true
                            else:
                                board[i][j] = '.' # Otherwise go back
     
                    return False
  
        return True
    

    def isValid(self, board, row, col, c):
        for i in range(9):
            if(board[i][col] != '.' and board[i][col] == c):
                return False; # check row
            if(board[row][i] != '.' and board[row][i] == c):
                return False; # check column
            if(board[3*(row//3)+i//3][3*(col//3)+i%3]!='.' and board[3*(row//3)+i//3][3*(col//3)+i%3]==c):
                return False # check 3*3 block
        
        return True