# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        def helper(node):

            if not node:
                return None
            
            node.left = helper(node.left)
            node.right = helper(node.right)

            node.left, node.right = node.right, node.left
        
            return node
        
        return helper(root)