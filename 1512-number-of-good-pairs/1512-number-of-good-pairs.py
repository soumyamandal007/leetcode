class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums), 1):
                if nums[j] == nums[i]:
                    count += 1
        return count