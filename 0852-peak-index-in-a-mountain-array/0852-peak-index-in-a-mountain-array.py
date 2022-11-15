class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx = 1
        while idx < len(arr):
            if arr[idx] > arr[idx-1]:
                idx += 1
            elif arr[idx] < arr[idx-1]:
                return idx-1