class Solution:
    def minimumOperations(self, num: str) -> int:
        min_opn = float("inf")
        s = list(num)
        print(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] == "5":
                for j in range(i-1,-1,-1):
                    if s[j] == "2" or s[j] == "7":
                        between = i - j - 1
                        later = len(s) - 1 - i
                        min_opn = min (min_opn, between+later)
                        break
            if s[i] == "0":
                for j in range(i-1,-1,-1):
                    if s[j] == "0" or s[j] == "5":
                        between = i - j - 1
                        later = len(s) - 1 - i
                        min_opn = min (min_opn, between+later)
                        break
        if min_opn == float("inf"):
            if "0" in s:
                return len(s) - 1
            else:
                return len(s)
        return min_opn