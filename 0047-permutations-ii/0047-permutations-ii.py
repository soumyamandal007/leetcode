class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counter = collections.Counter(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr)
            
            for key in counter:
                if counter[key]:
                    counter[key] -= 1
                    backtrack(curr + [key])
                    counter[key] += 1
        
        backtrack([])
        return ans
               