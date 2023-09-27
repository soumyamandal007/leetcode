class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)
        st = []
        for char in path:
            if char == "." or char == "":
                continue
            elif char == "..":
                if st:
                    st.pop()
            else:
                st.append(char)
        print(st)
        return "/"+"/".join(st)