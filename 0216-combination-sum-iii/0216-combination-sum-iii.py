class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []
        if k > n:
            return []
        nums = list(range(1,10))
        result = []
        print(nums)
        def backtrack(ind, ds, target):
            if target == 0 and len(ds) == k:
                result.append(ds[:])
                return
            for i in range(ind,len(nums)):
                if target < nums[i]:
                    break
                ds.append(nums[i])
                backtrack(i+1,ds,target-nums[i])
                ds.pop()
        backtrack(0,[],n)
        return result
        