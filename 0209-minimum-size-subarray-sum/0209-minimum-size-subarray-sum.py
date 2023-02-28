class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        until_sum = 78965467889
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                until_sum = min(until_sum,right-left+1)
                curr_sum -= nums[left]
                left += 1
        
        if until_sum == 78965467889:
            return 0
        else:
            return until_sum