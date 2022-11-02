class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(needle) -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[start:end+1] == needle:
                return (start)
                break
            start += 1
            end += 1
        return -1