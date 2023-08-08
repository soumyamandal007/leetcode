class Solution:
    def reverse(self,s,l,r):
            while l < r:
                s[l] , s[r] = s[r] , s[l]
                l += 1
                r -= 1
        
    def reverse_words(self,s):
        l = 0
        r = 0
        while l < len(s):
            while r < len(s) and s[r] != " ":
                r += 1
            self.reverse(s,l,r-1)
            l = r + 1
            r += 1
            
        
    def reverseWords(self, s: List[str]) -> None:
        
        self.reverse(s,0,len(s)-1)
        self.reverse_words(s)
        
        """Do not return anything, modify s in-place instead.
        """