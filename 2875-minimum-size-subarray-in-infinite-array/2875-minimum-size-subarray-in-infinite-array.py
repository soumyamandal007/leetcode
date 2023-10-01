class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        temp = nums + nums
        sum_nums = sum(nums)
        
        quo = target // sum_nums
        rem = target % sum_nums
        
        if not rem:
            return quo*len(nums) 
        
        target = rem
        
        res = float("inf")
        curr = 0
        j = 0
        for i in range(len(temp)):
            curr += temp[i]
            while curr > target:
                curr -= temp[j]
                j += 1
            if curr == target:
                res = min(res, i - j + 1)
        
        return -1 if res == float("inf") else quo*len(nums) + res 