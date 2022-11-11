import itertools as iter
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(1,len(nums)+1):
            newlist = list(iter.combinations(nums,i))
            for j in range(len(newlist)):
                res.append(list(newlist[j]))
        return res
