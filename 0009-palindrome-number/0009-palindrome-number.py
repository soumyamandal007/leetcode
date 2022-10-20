class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        flag = 10
        newX = 0
        while x > 0:
            mod = x % flag
            newX = newX*10 + mod
            x = x // 10
        if newX == temp:
            return True
        else:
            return False
            
        