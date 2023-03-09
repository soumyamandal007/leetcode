class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1 = s.split()
        print(s1)
        if len(pattern) != len(s1):
            return False
        p_s = {}
        s_p = {}
        for i,j in zip(pattern,s1):
            print(i,j)
            if (i not in p_s) and (j not in s_p):
                p_s[i] = j
                s_p[j] = i
            elif (p_s.get(i) != j) or (s_p.get(j) != i):
                return False
        return True
