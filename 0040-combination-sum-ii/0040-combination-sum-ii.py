class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(curr,s,i):
            if s > target:
                return
            if s == target:
                ans.append(curr[:])
            prev = -1
            for j in range(i,len(candidates)):
                if candidates[j] == prev:
                    continue
                curr.append(candidates[j])
                backtrack(curr,s+candidates[j],j+1)
                curr.pop()
                prev = candidates[j]
        
        backtrack([],0,0)
        return ans
            
    