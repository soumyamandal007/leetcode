class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        minSum = float("inf")

        # Calculate prefix minimums
        prefix = [nums[0]]
        for i in range(1, len(nums) - 1):
            prefix.append(min(prefix[-1], nums[i]))
        print(prefix)
        # Calculate suffix minimums
        suffix = [0] * (len(nums))
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            suffix[i] = min(suffix[i+1], nums[i])
        print(suffix)
        # Find the minimum sum of valid triplets
        for i in range(1, len(nums) - 1):
            if nums[i] > prefix[i-1] and nums[i] > suffix[i+1]:
                minSum = min(minSum, nums[i] + prefix[i-1] + suffix[i+1])
            print(minSum)

        if minSum == float("inf"):
            return -1
        else:
            return minSum
        