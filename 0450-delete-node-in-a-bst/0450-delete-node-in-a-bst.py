# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def remove(root,val):
            if not root:
                return None
            if val > root.val:
                root.right = remove(root.right,val)
            elif val < root.val:
                root.left = remove(root.left,val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    minN = minNode(root.right)
                    root.val = minN.val
                    root.right = remove(root.right,minN.val)
            return root
        return remove(root,key)







