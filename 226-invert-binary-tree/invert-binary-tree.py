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
            
            currLeft = node.left
            currRight = node.right

            if currLeft:
                node.right = currLeft
            else:
                node.right= None
            if currRight:
                node.left = currRight
            else:
                node.left = None

            helper(node.left)
            helper(node.right)

            return node
        
        return helper(root)
        
        
        