class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right -= 1
            else:
                left += 1
        return left