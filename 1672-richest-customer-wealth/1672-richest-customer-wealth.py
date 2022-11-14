class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        for i in range(len(accounts)):
            res = 0
            for j in range(len(accounts[0])):
                res += accounts[i][j]
            sum = max(sum,res)
        return sum