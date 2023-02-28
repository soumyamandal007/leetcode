class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for id,el in enumerate(nums):
            right_sum -= el
            if left_sum == right_sum:
                return id
            left_sum += el
        return -1
        


        