class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        print(nums)   
        count = 0
        for number in arr:
            if (number + 1) in nums:
                count += 1
        return count