class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_ind = 0
        max_ind = 0

        for i in range(indexDifference, len(nums)):
            if nums[i-indexDifference] < nums[min_ind]:
                min_ind = i - indexDifference
            if nums[i - indexDifference] > nums[max_ind]:
                max_ind = i - indexDifference
            
            if abs(nums[i] - nums[min_ind]) >= valueDifference:
                return [min_ind,i]
            if abs(nums[i] - nums[max_ind]) >= valueDifference:
                return [max_ind,i]

        return [-1,-1]        