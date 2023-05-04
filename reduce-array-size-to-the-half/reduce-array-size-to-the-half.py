class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = collections.Counter(arr)
        freq_val = sorted(counts.values(),reverse=True)
        print(freq_val)
        lensum = 0
        for i in range(len(freq_val)):
            lensum += freq_val[i]
            if lensum >= len(arr)//2:
                return i + 1
            print(lensum)