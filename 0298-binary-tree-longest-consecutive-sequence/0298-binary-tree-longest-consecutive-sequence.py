# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(node,length):
            if not node:
                return
            
            self.ans = max(self.ans, length)
            if node.left and node.left.val == node.val + 1:
                dfs(node.left, length+1)
            else:
                dfs(node.left,1)
            if node.right and node.right.val == node.val + 1:
                dfs(node.right, length+1)
            else:
                dfs(node.right,1)
        
        dfs(root,1)
        return self.ans