# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root or (not root.left and not root.right):
            return 0

        def helper(node, res, isLeft):

            if not node:
                return res
            
            if not node.left and not node.right and isLeft:
                res += node.val

            res = helper(node.left, res, True)
            res = helper(node.right, res, False)

            return res

        return helper(root, 0, False)