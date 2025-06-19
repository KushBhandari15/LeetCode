# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        res = 0

        def helper(node):
            nonlocal res
            if node is None:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            left_path = right_path = 0
            if node.left and node.left.val == node.val:
                left_path = left + 1
            if node.right and node.right.val == node.val:
                right_path = right + 1

            res = max(res, left_path + right_path)
            return max(left_path, right_path)

        helper(root)
        return res