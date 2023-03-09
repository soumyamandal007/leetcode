from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        countsRow = defaultdict(int)
        countsCol = defaultdict(int)

        for row in range(len(grid)):
            countsRow[tuple(grid[row])] += 1

        print(countsRow)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            countsCol[tuple(current_col)] += 1
        print(countsCol)
        ans = 0
        for array in countsRow:
            if array in countsCol:
                ans += countsCol[array] * countsRow[array]

        return ans