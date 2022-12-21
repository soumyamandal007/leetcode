class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[0]
        for i in range(1,len(nums),1):
            
            if nums[i] == n:
                return n
            else:
                n = nums[i]