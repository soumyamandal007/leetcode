class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        start = 0
        steps = 0
        water = capacity
        while start <= len(plants) - 1:
            if plants[start] <= water:
                steps += 1
                water -= plants[start]
                start += 1
            elif plants[start] > water:
                steps += start
                water = capacity
                steps += start + 1
                water -= plants[start]
                start += 1
        return steps
            
