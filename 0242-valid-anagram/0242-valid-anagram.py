class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}

        for keys in s:
            res[keys] = res.get(keys,0) + 1

        rs = {}
        for keys in t:
            rs[keys] = rs.get(keys,0) + 1
            
        if res == rs :
            return True
        else:
            return False