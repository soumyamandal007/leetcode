class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        def is_valid(arr):
            seen = set()
            for num in arr:
                if (1 <= num <= n) and num not in seen:
                    seen.add(num)
            if len(seen) != n:
                return False
            return True
            
        
        #check rows
        for row in matrix:
            if not is_valid(row):
                return False
        #checl cols
        
        for row in range(n):
            column = []
            for col in range(n):
                column.append(matrix[col][row])
            print(column)
            if not is_valid(column):
                return False
        
        return True
                
        
        