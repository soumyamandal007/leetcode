class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        print(count)
        heap = []
        
        for key, val in count.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for pair in heap:
            ans.append(pair[1])
        
        return ans