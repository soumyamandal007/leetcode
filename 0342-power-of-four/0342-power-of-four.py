class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return True
        if (n % 10 == 4 or n % 10 == 6) and n >= 16:
            return self.isPowerOfFour(n / 4)
        else:
            return False
        