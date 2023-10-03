class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        print(count)
        if min(count.values()) == 1:
            return -1
        opn = 0
        for c in count.values():
            opn += (c + 2) // 3
        return opn