# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        res = float('inf')

        def helper(node, depth):
            nonlocal res
            if not node:
                return

            # If it's a leaf node, update result
            if not node.left and not node.right:
                res = min(res, depth)
                return
            
            if node.left:
                helper(node.left, depth + 1)
            if node.right:
                helper(node.right, depth + 1)

        if not root:
            return 0

        helper(root, 1)
        return res
