# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -1001
        def helper(node):
            nonlocal res
            if node is None:
                return 0
            
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            curr = left + right + node.val
            res = max(curr, res)

            return node.val + max(left, right)
        
        helper(root)
        return res
