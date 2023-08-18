class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(arr):
            seen = set()
            for num in arr:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)
            return True
        
        #check rows
        for row in board:
            if not is_valid(row):
                return False
            
        #check cols
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not is_valid(column):
                return False
        
        
        #check sub- boxes
        for row in range(0,9,3):
            for col in range(0,9,3):
                sub_box = [board[i][j] for i in range(row,row+3) for j in range(col,col+3)]
                if not is_valid(sub_box):
                    return False
        return True