class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        res = []
        if not matrix:
            return res
        while top <= bottom and left <= right:
            
            #traverse top row
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
            
            #traverse right column
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            
            #traverse bottom row
            if top <= bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            #traverse left coloumn
            if left <= right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left += 1
        
        return res