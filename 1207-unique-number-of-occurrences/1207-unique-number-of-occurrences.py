class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for number in arr:
            if number in d:
                d[number] += 1
            else:
                d[number] = 1
        t = []
        for v in d.values():
            t.append(v)
        t.sort()
        freq = 1
        idx = 1
        while idx < len(t):
            if t[idx-1] == t[idx]:
                freq += 1
                idx += 1
                break
            else:
                freq = 1
                idx += 1
        if freq == 1:
            return True
        else:
            return False