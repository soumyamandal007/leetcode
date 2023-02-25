class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = [x for x in range(len(nums)+1)]
        print(n)
        for number in n:
            if number not in nums:
                return number