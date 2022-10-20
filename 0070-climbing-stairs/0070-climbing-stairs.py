class Solution:
    def climbStairs(self, n: int) ->int:
        if n == 1:
            currentValue = 1
        if n == 2:
            currentValue = 2
        if n>2:
            prevValue , currentValue = 0 , 1
            for i in range(n):
                latestValue = prevValue + currentValue
                prevValue = currentValue
                currentValue = latestValue
        return currentValue