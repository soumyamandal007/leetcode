class Solution:
    def romanToInt(self, s: str) -> int:
        count = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        print(count['M'])
        i = 0
        total = 0
        while i < len(s):
            if i + 1 < len(s) and count[s[i]] < count[s[i+1]]:
                total += count[s[i+1]] - count[s[i]]
                i += 2
            else:
                total += count[s[i]]
                i += 1
        return total