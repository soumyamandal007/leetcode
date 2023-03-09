from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(str)
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        sorted_tup = sorted(freq.items(), key=lambda x: x[1],reverse=True)
        print(sorted_tup)
        ans = ''
        for i,j in (sorted_tup):
            print(i,j)
            ans = ans + i*j
        return ans
            

        

        