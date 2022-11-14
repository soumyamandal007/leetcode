import itertools as iter
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        list1 = []
        for i in range(1,n+1):
            list1.append(i)
    
        comb = list(iter.combinations(list1,k))
        return comb