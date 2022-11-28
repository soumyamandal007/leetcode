class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for number in arr:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1
        print(d)
        res = []
        for k,v in d.items():
            if k == v:
                res.append(k)
        if res == []:
            return -1
        else:
            return max(res)