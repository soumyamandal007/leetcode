class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums += [float("inf"),float("-inf")]
        nums.sort()
        print(nums)
        count = 0
        for i in range(1,len(nums)):
            if nums[i-1] < i - 1 < nums[i]:
                count += 1
        return count