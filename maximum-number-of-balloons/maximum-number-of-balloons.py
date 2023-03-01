class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b , a , l, o, n = 1, 1, 2, 2, 1
        bcount = acount = lcount = ocount = ncount = 0

        for char in text:
            if char == 'b':
                bcount += 1
            if char == 'a':
                acount += 1
            if char == 'l':
                lcount += 1
            if char == 'o':
                ocount += 1
            if char == 'n':
                ncount += 1
        
        lcount = lcount // 2
        ocount = ocount // 2

        return min(bcount,acount,lcount,ocount,ncount)
        