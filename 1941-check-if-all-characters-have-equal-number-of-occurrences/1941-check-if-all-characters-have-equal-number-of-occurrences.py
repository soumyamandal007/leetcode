class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        val = list(d.values())
        print(d,val)
        ele = val[0]
        for element in val:
            if element != ele:
                return False
        return True
