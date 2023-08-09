class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            lo = 0
            hi = col
            while lo < hi :
                mid = (lo + hi)// 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
        return False