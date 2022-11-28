class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        print(n)
        res = []
        d = {}
        for number in nums:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1
        print(d)
        for k,v in d.items():
            if v > n:
                res.append(k)
        return res