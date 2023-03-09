class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}

        for i,j in zip(s,t):
            if (i not in s_t) and (j not in t_s):
                s_t[i] = j
                t_s[j] = i

            elif s_t.get(i) != j or t_s.get(j) != i:
                return False

        return True
