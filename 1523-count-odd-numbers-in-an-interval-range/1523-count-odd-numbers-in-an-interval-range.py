class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #even and even
        if low%2 == 0 and high%2 == 0:
            return (high-low)//2
        #odd and even
        elif low%2 != 0 and high%2 == 0:
            return (high-low)//2 + 1
        #even and odd
        elif low%2 == 0 and high%2 != 0:
            return (high-low)//2 + 1
        else:
            return (high-low)//2 + 1
        #odd and odd
