class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        print(row,col)
        onesRow = [0]*row
        zerosRow = [0]*row
        onesCol = [0]*col
        zerosCol = [0]*col
        print(onesRow,zerosRow)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
                else:
                    onesRow[i] += 1
                    onesCol[j] += 1
        print(zerosRow,onesRow,zerosCol,onesCol)
        #diff = [[0]*col]*row
        diff = []
        for i in range(row):
            r = []
            for j in range(col):
                difference = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
                r.append(difference)
            diff.append(r)
        return diff

