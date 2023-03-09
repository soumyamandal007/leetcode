class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count = collections.defaultdict(int)
        s2count = collections.defaultdict(int)
        for i in range(len(s1)):
            s1count[s1[i]] += 1
            s2count[s2[i]] += 1
        print(s1count,s2count)
        for i in range(len(s2)-len(s1)):
            print(s2count)
            if s1count == s2count:
                return True
            s2count[s2[i+len(s1)]] += 1
            s2count[s2[i]] -= 1
            if s2count[s2[i]] == 0:
                del s2count[s2[i]]
        if s1count == s2count:
            return True
        
        








        
        