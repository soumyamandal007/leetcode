class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        print(points)
        count = 1
        end = points[0][1]
        for point in points:
            if point[0] > end:
                count += 1
                end = point[1]
        return count
        