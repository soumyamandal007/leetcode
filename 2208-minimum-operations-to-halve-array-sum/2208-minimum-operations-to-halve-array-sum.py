class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-num for num in nums]
        target = sum(nums) / 2
        heapq.heapify(heap)
        
        ans = 0
        
        while target > 0:
            ans += 1
            pos = heapq.heappop(heap)
            target += pos / 2
            heapq.heappush(heap,pos/2)
        
        return ans
        