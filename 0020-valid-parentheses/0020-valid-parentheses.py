class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapdoor = {")":"(","}":"{","]":"["} #hashmap
        
        for c in s:
            if c in mapdoor:
                if stack and stack[-1] == mapdoor[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
                
        
        