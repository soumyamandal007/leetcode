class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        print(weight)
        wsum = 0
        for i in range(len(weight)):
            wsum += weight[i]
            print(wsum)
            if wsum > 5000:
                return i
            elif wsum == 5000:
                return i+1
            
        return len(weight)
        