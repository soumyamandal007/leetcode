class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        for w in word1:
            w1 += w
        w2 = ""
        for w in word2:
            w2 += w
        if w1 == w2:
            return True