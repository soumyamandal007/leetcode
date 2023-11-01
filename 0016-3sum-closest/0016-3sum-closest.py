class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closet_size = len(nums)
        diff = float("inf")
        nums.sort()
        print(nums)
        for i in range(0,closet_size-2):
            l = i + 1
            r = closet_size - 1
            while l < r:
                sum_three = nums[i] + nums[l] + nums[r]
                if abs(target - sum_three) < abs(diff):
                    diff = target - sum_three
                if sum_three < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0:
                break
        return target - diff
