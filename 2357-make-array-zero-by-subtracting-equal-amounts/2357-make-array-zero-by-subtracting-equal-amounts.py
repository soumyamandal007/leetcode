class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        for number in nums:
            if number != 0 :
                if number in d:
                    d[number] += 1
                else:
                    d[number] = 1
        return (len(d))
        
        