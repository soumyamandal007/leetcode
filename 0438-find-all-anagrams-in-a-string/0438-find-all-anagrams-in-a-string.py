class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls , lp = len(s) , len(p)
        
        if ls < lp:
            return []
        p_count = collections.Counter(p)
        s_count = collections.Counter()
        res = []
        
        for i in range(ls):
            s_count[s[i]] += 1
            if i > lp -1:
                if s_count[s[i-lp]] == 1:
                    del s_count[s[i-lp]]
                else:
                    s_count[s[i-lp]] -= 1
            if p_count == s_count:
                res.append(i-lp+1)
        return (res)
        