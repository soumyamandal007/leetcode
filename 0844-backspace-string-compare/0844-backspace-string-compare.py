class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildstack(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack and c == '#':
                    stack.pop()
            return stack
        
        return buildstack(s) == buildstack(t)