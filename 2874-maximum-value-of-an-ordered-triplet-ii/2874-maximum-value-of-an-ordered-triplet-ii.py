class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return 0
        
        left_min = [0] *n
        right_max = [0] *n
        left_min[0] = nums[0]
        right_max[-1] = nums[-1]
        for i in range(1,n):
            left_min[i] = max(nums[i],left_min[i-1])
        for k in range(n-2,-1,-1):
            right_max[k] = max(nums[k],right_max[k+1])
        print(left_min,right_max)
        
        res = 0
        for j in range(1,n-1):
            i = left_min[j-1]
            k = right_max[j+1]
            res = max(res,(i-nums[j])*k)
            
        return res
        
