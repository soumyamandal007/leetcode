from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        counts = defaultdict(int)
        ans = float("inf")
        for i in range(len(cards)):
            if cards[i] in counts:
                ans = min(ans, i - counts[cards[i]] +1)
            counts[cards[i]] = i
        
        if ans < float("inf"):
            return ans
        else:
            return -1
