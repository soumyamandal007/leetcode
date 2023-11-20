class Solution:
    def minimumSteps(self, s: str) -> int:
        one = 0
        count = 0
        for num in s:
            if num == '1':
                one += 1
            else:
                count += one
        
        return count
        