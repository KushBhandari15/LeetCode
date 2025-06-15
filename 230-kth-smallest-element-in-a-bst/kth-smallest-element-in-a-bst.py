# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        index = 0
        result = 0
        def helper(node):
            nonlocal index
            nonlocal result
            if node:
                helper(node.left)
                index += 1
                if index == k:
                    result = node.val
                helper(node.right)
        
        helper(root)
        return result