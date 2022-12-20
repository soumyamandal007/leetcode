class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        lower = nums[0]
        upper = nums[-1]
        print(lower,upper)
        gcd = 1
        for i in range(1,lower+1,1):
            if ((lower % i)==0 and (upper % i)==0):
                gcd = i
        return gcd