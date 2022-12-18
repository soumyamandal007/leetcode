class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = list(s.split())
        print(words)
        ans = ""
        for i in range(k):
            if i == k-1:
                ans += words[i] 
            else:
                ans += words[i] + " "
        return ans