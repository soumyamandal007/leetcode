class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        print(count)
        for i in range(count,len(nums),1):
            nums[i] = 0
        """
        Do not return anything, modify nums in-place instead.
        """