class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def checkDigits(number):
            count = 0
            while number != 0:
                number //= 10
                count += 1
            print(count)
            return count
        c = 0
        for num in nums:
            dig = checkDigits(num)
            if dig % 2 ==0:
                c += 1
        return c