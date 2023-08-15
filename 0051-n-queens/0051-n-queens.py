class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def placeNQueens(n, board, row, solutions):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return

            for i in range(n):
                if isSafe(row, i, board):
                    board[row][i] = 'Q'
                    placeNQueens(n, board, row + 1, solutions)
                    board[row][i] = '.'

        def isSafe(i, j, board):
            for r in range(len(board)):
                for c in range(len(board)):
                    if board[r][c] == 'Q' and (i == r or j == c or i + j == r + c or i - j == r - c):
                        return False
            return True

        qBoard = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        placeNQueens(n, qBoard, 0, solutions)
        return solutions