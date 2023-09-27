class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        right_half = []
        left_half = []
        n = len(nums)
        for i in range(k):
            left_half.append(nums[n-i-1])
        left_half.reverse()
        for i in range(n-k):
            right_half.append(nums[i])
        print(left_half , right_half)
        # nums = left_half + right_half
        # print(nums)
        for i in range(n):
            if i < k:
                nums[i] = left_half[i]
            else:
                nums[i] = right_half[i-k]
        """
        Do not return anything, modify nums in-place instead.
        """