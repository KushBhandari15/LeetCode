# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, low, high):

            if not node:
                return True
            
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            
            leftTree = helper(node.left, low, node.val)
            rightTree = helper(node.right, node.val, high)
        
            return leftTree and rightTree
        
        return helper(root, None, None)