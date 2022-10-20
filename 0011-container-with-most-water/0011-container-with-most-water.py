class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        flag = 0
        pos = len(height) - 1
        while pos > flag:
            area = min(height[flag],height[pos]) * (pos - flag)
            result = max(result,area)
            if height[flag] < height[pos]:
                flag += 1
            else:
                pos -= 1
                
        return result