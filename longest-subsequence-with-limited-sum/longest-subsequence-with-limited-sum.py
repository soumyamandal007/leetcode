class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pref = [nums[0]]
        for i in range(1,len(nums)):
            pref.append(pref[-1] + nums[i])
        print(pref)
        def bns(target):
            left = 0
            right = len(pref) - 1
            while left <= right:
                mid  = (left+right) // 2
                if target == pref[mid]:
                    return mid +1
                if target < pref[mid]:
                    right -= 1
                else:
                    left += 1
            return left
        ans= []
        for q in queries:
            pos = bns(q)
            print(pos)
            ans.append(pos)
            
        return ans
        