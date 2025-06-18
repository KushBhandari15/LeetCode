# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def helper(node, low, high):
            if not node:
                return True
            
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            left = helper(node.left, low, node.val)
            right = helper(node.right, node.val, high)

            return left and right
        
        return helper(root, None, None)
            
