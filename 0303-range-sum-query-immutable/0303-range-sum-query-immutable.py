class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        sum_until = 0
        for i in range(len(nums)):
            sum_until += nums[i]
            self.arr.append(sum_until)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self.arr[right] - self.arr[left-1]
        else:
            return self.arr[left or right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)