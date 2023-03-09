from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        counts = defaultdict(str)
        city = set()
        for strt, dest in paths:
            counts[strt] = dest
            city.add(strt)
            city.add(dest)

        for i in city:
            if i not in counts.keys():
                return i
