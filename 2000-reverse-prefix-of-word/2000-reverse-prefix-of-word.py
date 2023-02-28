class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        right = 0
        for i in range(len(word)):
            if word[i] == ch:
                right = i
                break
        print(right)
        w = list(word)
        print(w)
        left = 0
        while left < right:
            w[left] , w[right] = w[right] , w[left]
            left += 1
            right -= 1
        print(w)
        return "".join(w)