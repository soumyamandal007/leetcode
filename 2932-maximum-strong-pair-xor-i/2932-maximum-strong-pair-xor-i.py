class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        count = 0
        maxXor = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i],nums[j]):
                    count += 1
                    print(nums[i],nums[j])
                    maxXor = max(maxXor,nums[i]^nums[j])
        return maxXor
        