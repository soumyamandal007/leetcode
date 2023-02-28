class Solution:
    def reverseWords(self, s: str) -> str:
        wo_space = s.split(" ")
        print(wo_space)
        ans = []
        for s in wo_space:
            ans.append(s[::-1])
        print(ans)
        return " ".join(ans)