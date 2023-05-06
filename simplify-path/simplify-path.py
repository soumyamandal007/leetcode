class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        print(path.split("/"))
        for char in path.split("/"):
            if char == "..":
                if stack:
                    stack.pop()
            elif char == "." or not char:
                continue
            else:
                stack.append(char)
        print(stack)
        return "/"+"/".join(stack)