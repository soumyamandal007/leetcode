class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for r in range(1,numRows):
            rows.append([1]*(r+1))
            for c in range(1,r):
                rows[r][c] = rows[r-1][c] + rows[r-1][c-1]
        return rows