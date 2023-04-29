class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        def backtrack(curr,i):
            if i > len(nums):
                return
            ans.add(tuple(curr))
            for j in range(i,len(nums)):
                curr.append(nums[j])
                backtrack(curr, j+1)
                curr.pop()
        
        backtrack([],0)
        return list(ans)