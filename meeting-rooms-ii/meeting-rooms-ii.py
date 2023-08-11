class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [] , []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()
        print(start,end)
        count = 0
        maxCount = 0
        ps , pe = 0, 0
        while ps < len(start):
            if start[ps] < end[pe]:
                count += 1
                ps += 1
            else:
                count -= 1
                pe += 1
            maxCount = max(maxCount,count)
        return maxCount
        
        