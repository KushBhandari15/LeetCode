# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        if root is None:
            return res
        
        height = 0

        
        heightL = self.getHeightLeft(root, 0)
        heightR = self.getHeightRight(root, 0)
        if heightL == 1:
            return 1

        if heightL == heightR:
            nodes = 2**(heightL) - 1

        else:
            nodes = self.countNodes(root.left) + self.countNodes(root.right) + 1
            

        return nodes
    
    def getHeightLeft(self, node, height):
        if node:
            height += 1
            height = self.getHeightLeft(node.left, height)
        return height
    
    def getHeightRight(self, node, height):
        if node:
            height += 1
            height = self.getHeightRight(node.right, height)
        return height
