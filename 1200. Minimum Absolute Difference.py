class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        print(arr)
        diff = +math.inf
        for i in range(len(arr)-1):
            diff = min(diff,abs(arr[i]-arr[i+1]))
        print(diff)
        res = []
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1]) == diff:
                res.append([arr[i],arr[i+1]])
        return res
