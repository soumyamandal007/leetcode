class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = []
        while n != 0:
            dig = n % 10
            digits.append(dig)
            n //= 10
        print(digits)
        digits.reverse()
        print(digits)
        sum = 0
        flag = 1
        for i in range(len(digits)):
            sum += digits[i]*flag
            flag *= -1
        print(sum)
        return sum
            
        