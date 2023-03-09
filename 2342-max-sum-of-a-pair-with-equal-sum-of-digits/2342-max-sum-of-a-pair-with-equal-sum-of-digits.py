from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num != 0:
                digit = num % 10
                digit_sum += digit
                num = num // 10
            return digit_sum
        counts = defaultdict(int)
        ans = -1
        for num in nums:
            digit_sum = get_digit_sum(num)
            print(digit_sum)
            if digit_sum in counts:
                ans = max(ans,num + counts[digit_sum])
            counts[digit_sum] = max(num,counts[digit_sum])
        return ans


