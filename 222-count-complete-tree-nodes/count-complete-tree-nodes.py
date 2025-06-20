# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        if not root:
            return 0
        
        def helper(node):
            nonlocal res
            if node:
                helper(node.left)
                res += 1
                helper(node.right)
            
        helper(root)
        return res