# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        def helper(node, curr):
            if not node:
                return 0
            
            curr = curr*10 + node.val

            if node.left is None and node.right is None:
                return curr
            left = helper(node.left, curr)
            right = helper(node.right, curr)
            return left + right
        
        return helper(root, 0)