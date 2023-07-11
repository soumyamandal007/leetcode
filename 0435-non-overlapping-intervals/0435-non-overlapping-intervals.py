class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        count = 0
        m = -inf
        for interval in intervals:
            if interval[0] >= m:
                m = interval[1]
            else:
                count += 1
        return count
        