class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = collections.Counter(s)
        ans = []
        for char in order:
            ans.append(char*count[char])
            count[char] = 0
        
        for char in count:
            ans.append(char*count[char])
        
        return "".join(ans)


        