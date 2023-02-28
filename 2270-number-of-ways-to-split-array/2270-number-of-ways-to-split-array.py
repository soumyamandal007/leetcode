class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for i in range(1,len(nums)):
            pref.append(nums[i] + pref[-1])
        print(pref)
        ans = 0
        for i in range(len(pref)-1):
            left = pref[i]
            right = pref[-1] - pref[i]
            if left >= right:
                ans += 1
        return ans