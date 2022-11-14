class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less,equal,more = [],[],[]
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                more.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
        # less.sort(reverse = True)
        # more.sort()
        return less + equal + more