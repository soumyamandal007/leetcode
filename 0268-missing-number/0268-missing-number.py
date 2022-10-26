class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in range(0,n+1,1):
            res.append(i)
        for number in res:
            if number not in nums:
                return number
            