# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []

        def helper(node, curr):
            nonlocal res
            if not node:
                return
            
            curr += str(node.val)

            if not node.left and not node.right:
                res.append(curr)

            if node.left:
                helper(node.left, curr+"->")
            if node.right:
                helper(node.right, curr+"->")
        
        helper(root, "")
        return res

            