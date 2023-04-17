class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = [-num for num in nums]
        heapq.heapify(heap)
        while k > 0:
            x = heapq.heappop(heap)
            print(x)
            score += x
            heapq.heappush(heap, floor(x / 3))
            k -= 1
        
        return -score