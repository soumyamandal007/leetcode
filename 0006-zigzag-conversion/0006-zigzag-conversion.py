class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        #we have to find the rows in the matrix
        r = numRows
        #we have to find the columns
        l = len(s)
        section = ceil(l / (2*r - 2.0))
        c = section * (r - 1)
        mat = [[' '] * c for i in range(r)]       
        row = 0
        col = 0
        curr = 0
        
        while curr < l:
            #move down 
            while row < r and curr < l:
                mat[row][col] = s[curr]
                row += 1
                curr += 1
            row -= 2
            col += 1
            
            while row > 0 and col < c and curr < l:
                mat[row][col] = s[curr]
                row -= 1
                col += 1
                curr += 1
        ans = ""
        for row in mat:
            ans += "".join(row)
        return ans.replace(" ","")