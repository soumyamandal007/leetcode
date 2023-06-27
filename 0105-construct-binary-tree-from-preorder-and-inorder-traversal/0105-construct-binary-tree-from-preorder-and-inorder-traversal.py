# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        
        root.left = self.buildTree(preorder,inorder[:ind])
        root.right = self.buildTree(preorder,inorder[ind+1:]) 
        
        return root