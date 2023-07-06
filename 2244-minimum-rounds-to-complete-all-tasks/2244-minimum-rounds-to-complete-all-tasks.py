class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        freq = collections.defaultdict(int)
        for number in tasks:
            if number in freq:
                freq[number] += 1
            else:
                freq[number] = 1
        print(freq)
        for val in freq.values():
            if val == 1:
                return -1
            if val % 3 == 0:
                rounds += val // 3
            else:
                rounds += val // 3 + 1
        
        return rounds