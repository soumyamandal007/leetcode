class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        for s in range(len(nums)):
            min_ind = s
            for i in range(s+1,len(nums)):
                if nums[i] < nums[min_ind]:
                    min_ind = i
            nums[min_ind] , nums[s] = nums[s] , nums[min_ind]
        """
        Do not return anything, modify nums in-place instead.
        """
        