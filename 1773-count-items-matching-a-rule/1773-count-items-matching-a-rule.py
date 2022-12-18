class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for it in items:
            print(it)
            if ruleKey == "type":
                if it[0] == ruleValue:
                    count += 1
            elif ruleKey == "color":
                if it[1] == ruleValue:
                    count += 1
            elif ruleKey == "name":
                if it[2] == ruleValue:
                    count += 1
        return count
