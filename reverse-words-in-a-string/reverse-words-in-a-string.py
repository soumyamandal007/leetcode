class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split())
        print(words)
        res = ''
        for i in range(-1,-len(words)-1,-1):
            print(i)
            if i > -len(words):
                res += words[i] + ' '
            else:
                res += words[i]
        return res