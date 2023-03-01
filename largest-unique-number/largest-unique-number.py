from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for number in nums:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1

        print(counts)
        ans = -1
        for key in counts:
            if counts[key] == 1:
                ans = max(ans,key)
        
        return ans