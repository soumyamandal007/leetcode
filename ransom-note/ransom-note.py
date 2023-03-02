class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def dicti(s):
            d = {}
            for character in s:
                if character in d:
                    d[character] += 1
                else:
                    d[character] = 1
            return d
        ran = dicti(ransomNote)
        mag = dicti(magazine)
        print(ran,mag.keys())
        count = 0
        for k,v in ran.items():
            if k in mag.keys():
                print('yes',mag.get(k),v)
                if mag.get(k) >= v:
                    count += 1
        if count == len(ran):
            return True
          