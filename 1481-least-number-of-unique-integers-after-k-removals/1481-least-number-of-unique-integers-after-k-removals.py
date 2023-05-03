class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = collections.Counter(arr)
        freq_val = sorted(counts.values(),reverse=True)
        while k:
            val = freq_val[-1]
            if val <= k:
                k -= val
                freq_val.pop()
            else:
                break
        return len(freq_val)