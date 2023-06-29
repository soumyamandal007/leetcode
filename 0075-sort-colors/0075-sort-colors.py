class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        # for s in range(len(nums)):
        #     min_ind = s
        #     for i in range(s+1,len(nums)):
        #         if nums[i] < nums[min_ind]:
        #             min_ind = i
        #     nums[min_ind] , nums[s] = nums[s] , nums[min_ind]
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pos0 = 0
        curr = 0
        pos2 = len(nums) - 1
        
        while curr <= pos2:
            if nums[curr] == 0:
                nums[pos0] , nums[curr] = nums[curr] , nums[pos0]
                pos0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[pos2] , nums[curr] = nums[curr] , nums[pos2]
                pos2 -= 1
            else:
                curr += 1