class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        w1q = collections.deque(word1)
        w2q = collections.deque(word2)
        
        print(w1q,w2q)
        
        count = 1
        while w1q or w2q:
            if count % 2 != 0 and w1q:
                res += w1q.popleft()
            elif count % 2 == 0 and w2q:
                res += w2q.popleft()
            count += 1
        
        return (res)