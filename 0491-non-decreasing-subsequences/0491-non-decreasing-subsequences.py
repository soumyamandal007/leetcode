class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        ans = []
        def backtrack(ind):
            if ind == len(nums):
                if len(ans) >= 2:
                    res.add(tuple(ans))
                return
            if not ans or nums[ind] >= ans[-1]:
                ans.append(nums[ind])
                backtrack(ind+1)
                ans.pop()
            backtrack(ind+1)
        backtrack(0)
        return res
            
                
        