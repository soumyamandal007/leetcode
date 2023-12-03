class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        if len(mountain) == 1 or len(mountain) == 2:
            return []
        if len(mountain) == 3:
            if mountain[0] < mountain[1] and mountain[1] > mountain[2]:
                return [1]
            else:
                return []
        
        res = []
        for i in range(1,len(mountain)-1):
            print(i)
            if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]:
                res.append(i)
        return res