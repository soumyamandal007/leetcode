class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res.append(matrix[i][j])
                #print(res)
        high = len(res) - 1
        low = 0
        while high >= low:
            mid = (low+high) // 2
            if target < res[mid]:
                high = mid - 1
            elif target > res[mid]:
                low = mid + 1
            elif target == res[mid]:
                return (True)
            else:
                return (False)