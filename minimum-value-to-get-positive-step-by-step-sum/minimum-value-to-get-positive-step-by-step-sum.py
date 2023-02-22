class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        ans = 0
        for number in nums:
            sum += number
            ans = min(ans,sum) 
        return -ans+1