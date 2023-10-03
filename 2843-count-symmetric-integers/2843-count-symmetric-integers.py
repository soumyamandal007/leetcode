class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def lenDigit(num):
            n = str(num)
            l = len(n)
            if l % 2 != 0:
                return False
            leftsum , rightsum = 0, 0
            for i in range(len(n)//2):
                leftsum += int(n[i])
                rightsum += int(n[l-1-i])
            return leftsum == rightsum
        res = 0
        for n in range(low,high+1):
            if lenDigit(n):
                res += 1

        return res
