class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        print(count)
        count = sorted(count, key=lambda x:[-count[x],x])
        print(count)
        return count[:k]
