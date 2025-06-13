# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSibling(self, node, x, y):
        if not node:
            return False
        
        if node.left and node.right:
            if (node.left.val == x and node.right.val == y) or \
               (node.left.val == y and node.right.val == x):
                return True
        
        return self.isSibling(node.left, x, y) or self.isSibling(node.right, x, y)
    
    def getLevel(self, node, x, lev):
        if not node:
            return -1
        if node.val == x:
            return lev

        left_level = self.getLevel(node.left, x, lev + 1)
        if left_level != -1:
            return left_level
        
        return self.getLevel(node.right, x, lev + 1)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        lev1 = self.getLevel(root, x, 0)
        lev2 = self.getLevel(root, y, 0)
        
        if lev1 == -1 or lev2 == -1:
            return False
        
        return (lev1 == lev2) and not self.isSibling(root, x, y)
