# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            ret.append(node.val)
            dfs(node.right)
        
        dfs(root)
        print(ret)
        return ret[k-1]
        