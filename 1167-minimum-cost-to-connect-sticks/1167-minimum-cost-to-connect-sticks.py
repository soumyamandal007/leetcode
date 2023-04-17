class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0
        while len(sticks) >= 2:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            
            n = x + y
            ans += n
            heapq.heappush(sticks,n)
        return ans
        