class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def findSum(div):
            result = 0
            for num in nums:
                result += ceil(num/div)
            return result
        ans = -1
        low = 1
        high = max(nums)

        while low <= high:
            mid = (low+high) // 2
            r = findSum(mid)
            if r <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans