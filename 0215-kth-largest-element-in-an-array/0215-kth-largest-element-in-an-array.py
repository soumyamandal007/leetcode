import math
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        print(nums)
        #nums = list(dict.fromkeys(nums))
        print(nums)
        return nums[k-1]
       