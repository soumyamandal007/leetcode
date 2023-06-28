class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        letters = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        comb = []
        def backtrack (ind,path):
            if len(path) == len(digits):
                comb.append(''.join(path))
                return
            lett = letters[digits[ind]]
            for l in lett:
                path.append(l)
                backtrack(ind+1,path)
                path.pop()
            
        backtrack(0,[])
        
        return comb
        