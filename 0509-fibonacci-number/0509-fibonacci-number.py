class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            count = 0
            n1 = 0
            n2 = 1
            while count < n:
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
            return n1