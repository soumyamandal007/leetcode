class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])

        flat_vector = [element for row in grid for element in row]
        print(flat_vector)
        pref = [1]*len(flat_vector)
        # now start doing prefix product 
        for i in range(1,len(flat_vector)):
            pref[i] = (pref[i-1] * flat_vector[i-1]) % 12345
        print(pref)
        curr = 1
        for i in range(len(flat_vector)-2,-1,-1):
            curr *= flat_vector[i+1] % 12345
            pref[i]  *= curr % 12345
        print(pref)
        prod_mat = []
        k = 0
        for i in range(row):
            row = []
            for j in range(col):
                row.append(pref[k]%12345)
                k += 1
            prod_mat.append(row)
        return prod_mat