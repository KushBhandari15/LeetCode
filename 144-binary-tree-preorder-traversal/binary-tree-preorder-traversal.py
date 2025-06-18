# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def helper(node):
            nonlocal res
            if node:
                res.append(node.val)
                node.left = helper(node.left)
                node.right = helper(node.right)
        
        helper(root)
        return res