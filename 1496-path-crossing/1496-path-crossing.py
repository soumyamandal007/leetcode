from collections import defaultdict
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        strt = [0,0]
        counts = defaultdict(int)
        counts[tuple(strt)] = 1
        print(counts)
        for s in path:
            if s == 'N':
                strt[1] += 1
            elif s == 'S':
                strt[1] -= 1
            elif s == 'E':
                strt[0] += 1
            elif s == 'W':
                strt[0] -= 1
            if tuple(strt) in counts:
                return True
            else:
                counts[tuple(strt)] = 1 
        print(strt) 