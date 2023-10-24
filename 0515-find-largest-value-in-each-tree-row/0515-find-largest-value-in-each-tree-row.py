# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = collections.deque([root])
        while queue:
            curr_len = len(queue)
            curr_max = float("-inf")
            for i in range(curr_len): # for the whole level
                node = queue.popleft()
                curr_max = max(curr_max,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(curr_max) # after each level
        return ans