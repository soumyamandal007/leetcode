class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(curr,s,i):
            if s > target:
                return
            if s == target:
                ans.append(curr[:])
            for j in range(i,len(candidates)):
                curr.append(candidates[j])
                backtrack(curr,s + candidates[j], j)
                curr.pop()
            
        backtrack([],0,0)
        return ans
        