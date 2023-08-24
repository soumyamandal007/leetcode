class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        maxRight = [0] * n
        maxRight[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],nums[i+1])
        print(maxRight)
        maxLeft = nums[0]
        for i in range(1,n-1):
            if maxLeft < nums[i] < maxRight[i]:
                return True
            maxLeft = min(maxLeft,nums[i])
        return False