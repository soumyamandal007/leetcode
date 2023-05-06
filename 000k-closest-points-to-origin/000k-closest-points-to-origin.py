class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        d ={}
        for i in range(len(points)):
            d[i] = sqrt(pow(points[i][0],2)+pow(points[i][1],2))
        sorted_d = sorted(d.items(),key=lambda x:x[1])
        print(sorted_d)
        for i in range(k):
            res.append(points[sorted_d[i][0]])
        return res
    

        