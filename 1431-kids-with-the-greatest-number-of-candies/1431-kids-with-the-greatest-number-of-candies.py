class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [0]*len(candies)
        for i in range(len(candies)):
            candies[i] += extraCandies
            print(candies,max(candies))
            if candies[i] == max(candies):
                res[i] = True
            elif candies[i] < max(candies):
                res[i] = False
            candies[i] -= extraCandies
            print(candies,res)
        return res
        