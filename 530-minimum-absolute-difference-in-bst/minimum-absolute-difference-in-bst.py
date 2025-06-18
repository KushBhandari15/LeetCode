# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        prev = None

        def helper(node):
            nonlocal prev
            nonlocal res
            if node:
                helper(node.left)
                if prev is not None:
                    res = min(res, abs(node.val-prev))
                prev = node.val
                helper(node.right)
        
        helper(root)
        
        return res
        