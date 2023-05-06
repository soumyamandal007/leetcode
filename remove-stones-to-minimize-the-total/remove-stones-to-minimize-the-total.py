class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        
        while k > 0:
            pos = heapq.heappop(heap)
            pos = floor(pos / 2)
            print(pos)
            heapq.heappush(heap,pos)
            k -= 1
        print(heap)
        
        return -sum(heap)
        
        