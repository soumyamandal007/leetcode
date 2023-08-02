class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        left = 0
        res = 0
        count = collections.Counter()
        for i in range(len(nums)):
            count[nums[i]] += 1
            while len(count) == distinct:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            res += left
        return res
