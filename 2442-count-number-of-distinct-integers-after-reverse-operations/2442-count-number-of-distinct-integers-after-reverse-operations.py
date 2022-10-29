class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def rev(number):
            flag = 0
            while number > 0:
                digit = number % 10
                flag = flag*10 + digit
                number = number // 10   
            return flag

        for n in range(len(nums)):
            nums.append(rev(nums[n]))
        d = {}
        for number in nums:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1
        return (len(d))