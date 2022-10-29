class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d ={}
        for number in nums:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1

        for key,value in d.items():
            if value > len(nums)/2:
                return(key)
                break