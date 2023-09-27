class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = collections.defaultdict(int)
        for i,num in enumerate(nums):
            if num in count and abs(i - count[num]) <= k:
                return True
            count[num] = i
        
                

        