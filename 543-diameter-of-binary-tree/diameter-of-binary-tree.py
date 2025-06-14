# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.dia = 0

    def height(self, node):
        if node == None:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)

        curr = left+right+1
        self.dia = max(self.dia, curr)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.height(root)
        return self.dia - 1

    