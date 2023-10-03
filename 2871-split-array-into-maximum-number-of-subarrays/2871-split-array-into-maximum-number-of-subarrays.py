class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        count = 0
        mask = 2**32 - 1

        for num in  nums:
            mask &= num
            if mask == 0:
                count += 1
                mask = 2**32 - 1
        
        if count == 0:
            return 1
        else:
            return count
        