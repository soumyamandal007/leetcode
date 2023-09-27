class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {"(": ")", "[": "]", "{": "}"} #hashmap
        
        for char in s:
            if char in maps:
                stack.append(char)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if maps[prev] != char:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                
        
        