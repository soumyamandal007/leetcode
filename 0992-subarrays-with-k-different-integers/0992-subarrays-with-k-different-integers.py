class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atmost(k):
            freq = collections.defaultdict(int)
            left = 0
            count = 0
            for right in range(len(nums)):
                freq[nums[right]] += 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                if len(freq) <= k:
                    count += right - left + 1
            
            return count
        
        return atmost(k) - atmost(k-1)
                 