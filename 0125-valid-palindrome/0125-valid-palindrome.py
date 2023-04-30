class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(item for item in s if item.isalnum())
        s = s.lower()
        pal = ''
        for i in range(-1,-len(s)-1,-1):
            pal += ''.join(s[i])  
        print(pal,s)
        if pal == s:
            return True
        else:
            return False

