class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(dict.fromkeys(nums))
        if len(nums) == 1:
            return 1
        res = 0 
        start , end = 0, 1
        while end <= len(nums) - 1:
            if nums[end] == nums[end-1] + 1:
                end += 1
            elif nums[end] != nums[end-1] + 1:
                start = end
                end += 1
            res = max(res,end - start)
        return (res)