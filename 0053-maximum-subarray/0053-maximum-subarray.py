import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        sum_until = -math.inf
        for right in range(len(nums)):
            curr_sum += nums[right]
            if curr_sum>sum_until:
                sum_until = curr_sum
            if curr_sum<0:
                curr_sum = 0
        return sum_until