class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarysearch(tar):
            lo = 0
            hi = len(nums) - 1
            first_occurence = -1
            while lo <= hi :
                mid = (lo + hi) // 2
                if nums[mid] >= tar:
                    hi = mid - 1
                else:
                    lo = mid + 1
                if nums[mid] == tar:
                    first_occurence = mid
            return first_occurence
        def right(tar):
            lo = 0
            hi = len(nums) - 1
            last_occurence = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] <= tar:
                    lo = mid + 1
                else:
                    hi = mid - 1
                if nums[mid] == tar:
                    last_occurence = mid
            return last_occurence
            
        ans1 = binarysearch(target)
        ans2 = right(target)
        return [ans1,ans2]        