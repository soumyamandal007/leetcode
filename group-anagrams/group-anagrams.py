from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            print(key)
            anagram[key].append(s)
        
        return anagram.values()