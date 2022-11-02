class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d ={}
        for number in nums:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1
        true = 0
        for value in d.values():
            if value >= 2:
                true +=1
        if true != 0:
            return True
        else:
            return False