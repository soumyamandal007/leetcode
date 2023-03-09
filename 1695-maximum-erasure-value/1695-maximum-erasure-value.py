class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = 0
        left = 0
        number = set()
        curr = 0
        for right in range(len(nums)):
            while nums[right] in number:
                number.remove(nums[left])
                curr -= nums[left]
                left += 1
            curr += nums[right]
            number.add(nums[right])
            result = max(result,curr)
        return result
            
            
            