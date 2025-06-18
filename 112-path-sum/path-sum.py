# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        curr = root.val
        diff = targetSum - curr
        if not root.right and not root.left and diff == 0:
            return True

        left = self.hasPathSum(root.left, diff)
        right = self.hasPathSum(root.right, diff)

        return left or right