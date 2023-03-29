class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = collections.deque()
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            if queue[0] + k == i: #here we are using the sliding
                queue.popleft()
            
            if i >= k-1:
                ans.append(nums[queue[0]])

        return ans