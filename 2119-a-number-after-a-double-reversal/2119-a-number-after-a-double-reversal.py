class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # def rev(n):
        #     reverse = 0
        #     while n!= 0:
        #         reverse = reverse*10 + (n%10)
        #         n //= 10
        #     return reverse
        
        # first_rev = rev(num)
        # if num == rev(first_rev):
        #     return True
        if num == 0:
            return True
        if num % 10 != 0:
            return True