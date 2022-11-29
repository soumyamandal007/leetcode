class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        count = 0
        #XY plane 
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    count += 1
        print(count)
        #XZ plane
        for i in range(len(grid)):
            count += max(grid[i])
        print(count)
        #YZ plane , max cols
        for i in range(len(grid)):
            colmax = 0
            for j in range(len(grid)):
                colmax = max(colmax,grid[j][i])
                print(grid[j][i], '/')
            print(colmax)
            count += colmax
        print(count)
        return count