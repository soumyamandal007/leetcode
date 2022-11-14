import numpy
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        while n != 0:
            digits.append(n%10)
            n = n // 10
        prod = 1
        for i in range(len(digits)):
            prod *= digits[i]
        sum = 0
        for i in range(len(digits)):
            sum += digits[i]

        return (prod - sum)
