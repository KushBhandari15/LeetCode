# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        arr = []
        def helper(node):
            nonlocal arr
            if node:
                helper(node.left)
                arr.append(node.val)
                helper(node.right)
        
        helper(root)
        for i in range (1, len(arr)):
            res = min(res, abs(arr[i]-arr[i-1]))
            if res == 0:
                return 0
        
        return res
        