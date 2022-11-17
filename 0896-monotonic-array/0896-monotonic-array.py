class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        count , rev = 0 , 0
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                count += 1
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                rev += 1 

        if count == len(nums) - 1 or rev == len(nums) - 1:
            return True