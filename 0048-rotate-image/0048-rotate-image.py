class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        temp = []
        for i in range(len(matrix[0])):
            row = []
            for item in matrix:
                row.append(item[i])
            temp.append(row)
        print(temp)
        for i in range(len(temp)):
            print(temp[i])
            row = []
            for j in range(-1,-len(temp[i])-1,-1):
                print(temp[i][j])
                row.append(temp[i][j])
            matrix[i] = row
        print(matrix)
         
        """
        Do not return anything, modify matrix in-place instead.
        """