class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for number in nums:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1
        print(d)
        sum = 0
        for key,value in d.items():
            if value == 1:
                sum += key
        return sum