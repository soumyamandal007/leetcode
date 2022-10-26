class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freqCount(string):
            d = {}
            for s in string:
                if s in d:
                    d[s] +=1
                else:
                    d[s] = 1
            return d
        count = []
        for string in strs:
            count.append((freqCount(string)))
        temp = (count)
        res = []
        row = 0
        for i in range(len(count)):
            r = []
            for j in range(len(temp)):
                if count[i] == temp[j]:
                    r.append(strs[j])
                    res.append(r)
            row += 1
#res = list(dict.fromkeys(res))
        dupFree = []
        for li in res:
            if li not in dupFree:
                dupFree.append(li)
        return dupFree