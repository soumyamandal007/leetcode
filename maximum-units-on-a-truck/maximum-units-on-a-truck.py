class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse=True)
        print(boxTypes)
        total = 0
        for i in range(len(boxTypes)):
            if truckSize:
                if boxTypes[i][0] <= truckSize:
                    total += boxTypes[i][0]*boxTypes[i][1]
                    truckSize -= boxTypes[i][0]
                else:
                    total += truckSize*boxTypes[i][1]
                    truckSize = 0
        return total
        