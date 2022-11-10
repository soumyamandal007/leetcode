class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(array):
            array.sort()
            diff = array[1] - array[0]
            for j in range(len(array)-1):
                if array[j+1] - array[j] != diff:
                    return False
            return True    
            
        results = []
        for i in range(len(l)):
            results.append(check(nums[l[i]:r[i]+1]))
        return (results)
