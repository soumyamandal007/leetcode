class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > start + k:
                start = nums[i]
                ans += 1
        return ans