from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        def rowsCheck():
            for i in range(rows):
                sudoku = set()

                for j in range(cols):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in sudoku:
                        return False

                    sudoku.add(board[i][j])

            return True

        def colsCheck():
            for i in range(cols):
                sudoku = set()

                for j in range(rows):
                    if board[j][i] == ".":
                        continue

                    if board[j][i] in sudoku:
                        return False

                    sudoku.add(board[j][i])

            return True

        def boxCheck():
            for i in range(3):
                for j in range(3):

                    sudoku = set()

                    for k in range(3):
                        for l in range(3):

                            value = board[i*3+k][j*3+l]

                            if value == ".":
                                continue

                            if value in sudoku:
                                return False

                            sudoku.add(value)

            return True

        return rowsCheck() and colsCheck() and boxCheck()