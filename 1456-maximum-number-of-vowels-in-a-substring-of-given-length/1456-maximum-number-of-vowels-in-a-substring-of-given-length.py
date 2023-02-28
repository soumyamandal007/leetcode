class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k
        ans = 0
        max_ans = 0
        vowels = ['a','e','i','o','u']
        for i in range(left,right):
            if s[i] in vowels:
                ans += 1
        print(ans)
        max_ans = max(max_ans,ans)
        for i in range(k,len(s)):
            print(s[i])
            if s[i] in vowels:
                ans += 1
            if s[left] in vowels:
                ans -= 1

            left += 1
            max_ans = max(ans,max_ans)
            print(max_ans)
        return max_ans







        